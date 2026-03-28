"""
Allen-Bradley / Rockwell Automation Manual Downloader
======================================================
Downloads PDF manuals from Rockwell's public Literature Library.

Usage:
    python downloader.py                          # Download all families
    python downloader.py --family controllogix    # Single family
    python downloader.py --family powerflex_750_series powerflex_520_series
    python downloader.py --list                   # List available families
    python downloader.py --dry-run                # Preview without downloading
    python downloader.py --resume                 # Skip already-downloaded files

IMPORTANT: This script downloads from Rockwell's public Literature Library.
           You must be an authorized Rockwell customer. Downloaded PDFs are
           for your personal/organizational use only. Do not redistribute.
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

import certifi
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ── Try to import catalog ────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
base = os.path.dirname(__file__)
print(base)
from publications import PUBLICATIONS, get_all_publications, list_families

# ── Configuration ────────────────────────────────────────────────────────────

BASE_URLS = [
    # Primary (newer URL pattern)
    "https://literature.rockwellautomation.com/idc/groups/literature/documents/{pub_type}/{pub_num}_-en-p.pdf",
    # Fallback 1 (without underscore separator)
    "https://literature.rockwellautomation.com/idc/groups/literature/documents/{pub_type}/{pub_num}-en-p.pdf",
    # Fallback 2 (some docs use this pattern)
    "https://literature.rockwellautomation.com/idc/groups/literature/documents/{pub_type}/{pub_num}c-en-p.pdf",
]

OUTPUT_DIR = Path("docs")
LOG_DIR = Path("logs")
STATE_FILE = Path("logs/download_state.json")

# Polite rate limiting — don't hammer their servers
DELAY_BETWEEN_REQUESTS = 2.0   # seconds between each download
DELAY_ON_RETRY = 5.0           # seconds before retry after failure
MAX_RETRIES = 3
REQUEST_TIMEOUT = 30           # seconds
CHUNK_SIZE = 8192              # bytes for streaming download

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ABManualDownloader/1.0; "
                  "personal-use-rag-project)",
    "Accept": "application/pdf,*/*",
}

# ── Logging Setup ────────────────────────────────────────────────────────────

def setup_logging():
    LOG_DIR.mkdir(exist_ok=True)
    log_file = LOG_DIR / f"download_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout),
        ],
    )
    return logging.getLogger("ab_downloader")


# ── HTTP Session ─────────────────────────────────────────────────────────────

def build_session():
    session = requests.Session()
    retry = Retry(
        total=MAX_RETRIES,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(HEADERS)
    session.trust_env = False  # ignore CURL_CA_BUNDLE / REQUESTS_CA_BUNDLE env vars
    session.verify = certifi.where()
    return session


# ── State / Progress Tracking ────────────────────────────────────────────────

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"downloaded": [], "failed": [], "not_found": []}


def save_state(state):
    STATE_FILE.parent.mkdir(exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ── Download Logic ───────────────────────────────────────────────────────────

def try_download_url(session, url, dest_path, logger):
    """Attempt to download from a single URL. Returns True on success."""
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT, stream=True)

        if response.status_code == 404:
            return False, "404"

        response.raise_for_status()

        # Verify it's actually a PDF
        content_type = response.headers.get("Content-Type", "")
        if "pdf" not in content_type.lower() and "octet-stream" not in content_type.lower():
            # Check first bytes
            first_chunk = b""
            for chunk in response.iter_content(CHUNK_SIZE):
                first_chunk = chunk
                break
            if not first_chunk.startswith(b"%PDF"):
                return False, "not_pdf"

        # Stream to disk
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = dest_path.with_suffix(".tmp")

        with open(tmp_path, "wb") as f:
            if "first_chunk" in dir():
                f.write(first_chunk)
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:
                    f.write(chunk)

        # Validate file size (reject tiny/empty files)
        size = tmp_path.stat().st_size
        if size < 5000:  # Less than 5KB is almost certainly not a real manual
            tmp_path.unlink()
            return False, "too_small"

        tmp_path.rename(dest_path)
        return True, size

    except requests.exceptions.Timeout:
        return False, "timeout"
    except requests.exceptions.ConnectionError:
        return False, "connection_error"
    except requests.exceptions.HTTPError as e:
        return False, f"http_{e.response.status_code}"
    except Exception as e:
        return False, str(e)


def download_manual(session, family, pub_type, pub_num, output_dir, logger, dry_run=False):
    """
    Try all URL patterns for a given publication.
    Returns: 'downloaded', 'skipped', 'not_found', 'failed'
    """
    family_dir = output_dir / family
    filename = f"{pub_num}-en-p.pdf"
    dest_path = family_dir / filename

    if dest_path.exists():
        logger.debug(f"  SKIP  {pub_num} (already exists)")
        return "skipped", dest_path

    if dry_run:
        urls = [u.format(pub_type=pub_type, pub_num=pub_num) for u in BASE_URLS]
        logger.info(f"  DRY   {pub_num} → {urls[0]}")
        return "dry_run", None

    # Try each URL pattern
    for url_template in BASE_URLS:
        url = url_template.format(pub_type=pub_type, pub_num=pub_num)
        logger.info(f"  GET   {url}")

        success, result = try_download_url(session, url, dest_path, logger)

        if success:
            size_kb = result / 1024
            logger.info(f"  ✓ OK  {filename}  ({size_kb:.0f} KB)")
            return "downloaded", dest_path

        if result == "404":
            continue  # Try next URL pattern
        else:
            logger.warning(f"  ✗ ERR {filename}: {result}")
            time.sleep(DELAY_ON_RETRY)

    logger.warning(f"  ✗ NOT FOUND: {pub_num} (tried {len(BASE_URLS)} URL patterns)")
    return "not_found", None


# ── Main Runner ──────────────────────────────────────────────────────────────

def run_download(families, output_dir, dry_run=False, resume=True):
    logger = setup_logging()
    logger.info("=" * 60)
    logger.info("Allen-Bradley Manual Downloader")
    logger.info(f"Output dir : {output_dir.resolve()}")
    logger.info(f"Families   : {', '.join(families)}")
    logger.info(f"Dry run    : {dry_run}")
    logger.info(f"Resume     : {resume}")
    logger.info("=" * 60)

    output_dir.mkdir(exist_ok=True)
    state = load_state() if resume else {"downloaded": [], "failed": [], "not_found": []}
    session = build_session()

    # Build work list
    work = []
    for family in families:
        if family not in PUBLICATIONS:
            logger.error(f"Unknown family: '{family}'. Use --list to see available families.")
            continue
        for pub_type, pub_num in PUBLICATIONS[family]:
            work.append((family, pub_type, pub_num))

    total = len(work)
    counts = {"downloaded": 0, "skipped": 0, "not_found": 0, "failed": 0, "dry_run": 0}

    logger.info(f"\nTotal publications to process: {total}\n")

    for i, (family, pub_type, pub_num) in enumerate(work, 1):
        logger.info(f"[{i:3d}/{total}] {family} / {pub_num}")

        # Skip if already recorded as downloaded
        if resume and pub_num in state["downloaded"]:
            logger.info(f"  SKIP  {pub_num} (in state file)")
            counts["skipped"] += 1
            continue

        status, path = download_manual(
            session, family, pub_type, pub_num, output_dir, logger, dry_run
        )

        counts[status] = counts.get(status, 0) + 1

        if status == "downloaded":
            state["downloaded"].append(pub_num)
            save_state(state)
        elif status == "not_found":
            if pub_num not in state["not_found"]:
                state["not_found"].append(pub_num)
            save_state(state)
        elif status == "failed":
            if pub_num not in state["failed"]:
                state["failed"].append(pub_num)
            save_state(state)

        # Polite delay between requests
        if status not in ("skipped", "dry_run") and i < total:
            time.sleep(DELAY_BETWEEN_REQUESTS)

    # ── Summary ──────────────────────────────────────────────────────────────
    logger.info("\n" + "=" * 60)
    logger.info("DOWNLOAD COMPLETE")
    logger.info(f"  Downloaded : {counts.get('downloaded', 0)}")
    logger.info(f"  Skipped    : {counts.get('skipped', 0)}")
    logger.info(f"  Not found  : {counts.get('not_found', 0)}")
    logger.info(f"  Failed     : {counts.get('failed', 0)}")
    if dry_run:
        logger.info(f"  Dry run    : {counts.get('dry_run', 0)}")

    # Count files on disk
    if not dry_run:
        pdf_count = sum(1 for _ in output_dir.rglob("*.pdf"))
        total_mb = sum(f.stat().st_size for f in output_dir.rglob("*.pdf")) / (1024 * 1024)
        logger.info(f"\nDocs on disk: {pdf_count} PDFs  ({total_mb:.1f} MB)")

    logger.info("=" * 60)
    return counts


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    global DELAY_BETWEEN_REQUESTS
    parser = argparse.ArgumentParser(
        description="Download Allen-Bradley manuals from Rockwell Literature Library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python downloader.py                                  Download ALL families
  python downloader.py --family controllogix            Single family
  python downloader.py --family controllogix compactlogix powerflex_750_series
  python downloader.py --list                           List available families
  python downloader.py --dry-run                        Preview URLs only
  python downloader.py --no-resume                      Re-download everything
  python downloader.py --output /mnt/manuals            Custom output directory
        """,
    )
    parser.add_argument(
        "--family", nargs="+", metavar="FAMILY",
        help="Product family/families to download (default: all)"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List all available product families and exit"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print URLs that would be downloaded without actually downloading"
    )
    parser.add_argument(
        "--no-resume", action="store_true",
        help="Ignore previous state and re-download everything"
    )
    parser.add_argument(
        "--output", default="docs", metavar="DIR",
        help="Output directory for downloaded PDFs (default: ./docs)"
    )
    parser.add_argument(
        "--delay", type=float, default=DELAY_BETWEEN_REQUESTS, metavar="SECONDS",
        help=f"Delay between requests in seconds (default: {DELAY_BETWEEN_REQUESTS})"
    )

    args = parser.parse_args()

    if args.list:
        print("\nAvailable product families:\n")
        for family in sorted(list_families()):
            count = len(PUBLICATIONS[family])
            print(f"  {family:<35} ({count} publications)")
        print()
        return

    DELAY_BETWEEN_REQUESTS = args.delay

    families = args.family if args.family else list_families()

    run_download(
        families=families,
        output_dir=Path(args.output),
        dry_run=args.dry_run,
        resume=not args.no_resume,
    )


if __name__ == "__main__":
    main()