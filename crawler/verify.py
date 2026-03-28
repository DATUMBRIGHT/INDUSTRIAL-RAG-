"""
AB Manual Collection Verifier & Manifest Generator
====================================================
Verifies downloaded PDFs are valid and generates a manifest
for use by the RAG ingestion pipeline.

Usage:
    python verify.py                        # Verify all docs/ PDFs
    python verify.py --output docs/         # Specify docs directory
    python verify.py --manifest             # Generate manifest.json
    python verify.py --report              # Print detailed report
"""

import argparse
import json
import logging
import struct
import sys
from datetime import datetime
from pathlib import Path

logger = logging.getLogger("ab_verifier")


def is_valid_pdf(path: Path) -> tuple[bool, str]:
    """Check if file is a valid PDF."""
    try:
        with open(path, "rb") as f:
            header = f.read(8)
            if not header.startswith(b"%PDF"):
                return False, "not_a_pdf"

            # Check file size
            size = path.stat().st_size
            if size < 5000:
                return False, f"too_small_{size}b"

            # Try to find EOF marker
            f.seek(-128, 2)  # Last 128 bytes
            tail = f.read()
            if b"%%EOF" not in tail and b"%EOF" not in tail:
                # Some PDFs don't have clean EOF, not necessarily invalid
                pass

            return True, f"ok_{size}"
    except Exception as e:
        return False, f"error_{e}"


def extract_pdf_metadata(path: Path) -> dict:
    """Extract basic metadata from PDF without external deps."""
    metadata = {
        "size_bytes": path.stat().st_size,
        "size_kb": round(path.stat().st_size / 1024, 1),
        "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
    }

    try:
        with open(path, "rb") as f:
            # Read first 4KB looking for Title/Author in PDF metadata
            content = f.read(4096).decode("latin-1", errors="ignore")

            # Extract PDF version
            version_match = __import__("re").search(r"%PDF-(\d+\.\d+)", content)
            if version_match:
                metadata["pdf_version"] = version_match.group(1)

            # Look for /Title in metadata
            title_match = __import__("re").search(r"/Title\s*\(([^)]+)\)", content)
            if title_match:
                metadata["title"] = title_match.group(1).strip()

    except Exception:
        pass

    return metadata


def infer_pub_info(filepath: Path) -> dict:
    """Infer publication info from filename and path."""
    family = filepath.parent.name
    filename = filepath.stem  # e.g. "1756-um001-en-p"

    import re
    # Pattern: {catalog}-{type}{num}-en-p
    match = re.match(r"^([\w-]+?)-(um|rm|pm|in|qr|td|ap|sr|pp)(\d+)", filename, re.I)

    if match:
        return {
            "family": family,
            "catalog_prefix": match.group(1),
            "pub_type": match.group(2).lower(),
            "pub_num_raw": filename,
        }

    return {"family": family, "pub_num_raw": filename}


def verify_collection(docs_dir: Path) -> dict:
    """Verify all PDFs in the collection."""
    docs_dir = Path(docs_dir)
    if not docs_dir.exists():
        logger.error(f"Directory not found: {docs_dir}")
        return {}

    results = {
        "valid": [],
        "invalid": [],
        "total_size_mb": 0,
        "by_family": {},
    }

    pdf_files = sorted(docs_dir.rglob("*.pdf"))
    logger.info(f"Found {len(pdf_files)} PDF files in {docs_dir}")

    for pdf_path in pdf_files:
        valid, status = is_valid_pdf(pdf_path)
        metadata = extract_pdf_metadata(pdf_path)
        pub_info = infer_pub_info(pdf_path)

        entry = {
            "path": str(pdf_path.relative_to(docs_dir)),
            "filename": pdf_path.name,
            "status": status,
            "valid": valid,
            **pub_info,
            **metadata,
        }

        family = pub_info.get("family", "unknown")
        if family not in results["by_family"]:
            results["by_family"][family] = {"count": 0, "size_mb": 0, "files": []}

        results["by_family"][family]["count"] += 1
        results["by_family"][family]["size_mb"] += metadata["size_kb"] / 1024
        results["by_family"][family]["files"].append(entry)

        results["total_size_mb"] += metadata["size_kb"] / 1024

        if valid:
            results["valid"].append(entry)
            logger.debug(f"  ✓ {pdf_path.name} ({metadata['size_kb']} KB)")
        else:
            results["invalid"].append(entry)
            logger.warning(f"  ✗ {pdf_path.name} — {status}")

    return results


def generate_manifest(docs_dir: Path, output_path: Path = None):
    """
    Generate a manifest.json for use by the RAG ingestion pipeline.
    Each entry includes path, family, pub_num, and metadata.
    """
    results = verify_collection(docs_dir)
    docs_dir = Path(docs_dir)

    manifest = {
        "generated": datetime.now().isoformat(),
        "docs_dir": str(docs_dir.resolve()),
        "total_documents": len(results.get("valid", [])),
        "total_size_mb": round(results.get("total_size_mb", 0), 2),
        "invalid_count": len(results.get("invalid", [])),
        "families": list(results.get("by_family", {}).keys()),
        "documents": results.get("valid", []),
    }

    if output_path is None:
        output_path = docs_dir / "manifest.json"

    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)

    logger.info(f"Manifest written: {output_path}")
    logger.info(f"  {manifest['total_documents']} valid documents")
    logger.info(f"  {manifest['total_size_mb']:.1f} MB total")
    logger.info(f"  {manifest['invalid_count']} invalid files")

    return manifest


def print_report(docs_dir: Path):
    """Print a detailed human-readable report."""
    results = verify_collection(docs_dir)

    print("\n" + "=" * 60)
    print("AB MANUAL COLLECTION REPORT")
    print("=" * 60)
    print(f"Directory  : {Path(docs_dir).resolve()}")
    print(f"Valid PDFs : {len(results.get('valid', []))}")
    print(f"Invalid    : {len(results.get('invalid', []))}")
    print(f"Total Size : {results.get('total_size_mb', 0):.1f} MB")
    print()

    print("By Product Family:")
    print("-" * 40)
    for family, info in sorted(results.get("by_family", {}).items()):
        print(f"  {family:<35} {info['count']:>3} docs  {info['size_mb']:.1f} MB")

    if results.get("invalid"):
        print("\nInvalid Files:")
        print("-" * 40)
        for entry in results["invalid"]:
            print(f"  ✗ {entry['filename']} — {entry['status']}")

    print("=" * 60)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        handlers=[logging.StreamHandler()],
    )

    parser = argparse.ArgumentParser(
        description="Verify Allen-Bradley manual collection and generate manifest"
    )
    parser.add_argument("--output", default="docs", metavar="DIR", help="Docs directory (default: docs)")
    parser.add_argument("--manifest", action="store_true", help="Generate manifest.json for RAG pipeline")
    parser.add_argument("--manifest-out", metavar="FILE", help="Custom manifest output path")
    parser.add_argument("--report", action="store_true", help="Print detailed collection report")
    parser.add_argument("--quiet", action="store_true", help="Minimal output")

    args = parser.parse_args()

    if args.quiet:
        logging.getLogger().setLevel(logging.WARNING)

    docs_dir = Path(args.output)

    if args.report:
        print_report(docs_dir)
    elif args.manifest:
        out = Path(args.manifest_out) if args.manifest_out else None
        generate_manifest(docs_dir, out)
    else:
        # Default: verify and show summary
        results = verify_collection(docs_dir)
        valid = len(results.get("valid", []))
        invalid = len(results.get("invalid", []))
        total_mb = results.get("total_size_mb", 0)
        print(f"\nCollection: {valid} valid, {invalid} invalid, {total_mb:.1f} MB total")
        if invalid:
            print("Run with --report to see invalid files")
        print("Run with --manifest to generate RAG pipeline manifest")


if __name__ == "__main__":
    main()