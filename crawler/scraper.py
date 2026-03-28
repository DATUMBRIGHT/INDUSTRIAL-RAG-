"""
Rockwell Literature Library Discovery Scraper
=============================================
Discovers publication numbers by scraping the Rockwell Literature Library
search/browse pages. Use this to find manuals NOT in the static catalog.

This supplements the static catalog in publications.py with dynamically
discovered publications.

Usage:
    python scraper.py --search "PowerFlex 755"
    python scraper.py --catalog-num 750          # Search by catalog number prefix
    python scraper.py --discover-all             # Try to discover everything (slow)
    python scraper.py --export discovered.json   # Save results to JSON
"""

import argparse
import json
import logging
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlencode, urljoin

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger("ab_scraper")

# ── Rockwell Literature Library API ─────────────────────────────────────────
# The Literature Library uses a search endpoint that returns JSON

SEARCH_API = "https://literature.rockwellautomation.com/api/search"
BROWSE_URL = "https://www.rockwellautomation.com/en-us/support/documentation/literature-library.html"

# Known product catalog number prefixes to sweep
CATALOG_PREFIXES = [
    # ControlLogix
    "1756",
    # CompactLogix
    "1769",
    # MicroLogix
    "1766", "1764", "1763", "1762",
    # Micro800
    "2080",
    # PowerFlex
    "20b", "20f", "20g", "22a", "22b", "22c", "22f",
    "520", "523", "525", "750", "753", "755",
    # Kinetix
    "2094", "2097", "2098", "2198",
    # PanelView
    "2711", "2711p", "2711r",
    # I/O
    "1734", "1794", "1797",
    # Safety
    "1791", "1791es", "440c", "440r",
    # SLC/PLC legacy
    "1747", "1746", "1785",
    # Drives
    "1336",
    # Networking
    "1783", "1788",
]

# Publication type suffixes to try
PUB_TYPES = ["um", "rm", "pm", "in", "qr", "td", "ap", "sr", "pp"]

DELAY = 1.5  # seconds between requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ABManualScraper/1.0; personal-use)",
    "Accept": "application/json, text/html, */*",
}


class LiteratureDiscoverer:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.discovered = {}  # pub_num -> metadata

    def search(self, query, max_results=50):
        """Search the literature library for publications matching a query."""
        logger.info(f"Searching: '{query}'")

        try:
            # Try the JSON API first
            params = {
                "q": query,
                "rows": max_results,
                "start": 0,
                "lang": "en",
            }
            resp = self.session.get(SEARCH_API, params=params, timeout=15)

            if resp.status_code == 200:
                try:
                    data = resp.json()
                    return self._parse_api_response(data)
                except json.JSONDecodeError:
                    pass

            # Fallback: parse HTML
            return self._search_html(query)

        except Exception as e:
            logger.warning(f"Search failed for '{query}': {e}")
            return []

    def _parse_api_response(self, data):
        """Parse JSON API response."""
        results = []
        docs = data.get("response", {}).get("docs", []) or data.get("docs", []) or []

        for doc in docs:
            pub_num = doc.get("pubNumber") or doc.get("pub_number") or doc.get("id", "")
            if not pub_num:
                continue

            # Clean up pub number
            pub_num = pub_num.lower().strip()
            pub_num = re.sub(r'[_\s]+', '-', pub_num)
            pub_num = re.sub(r'-en-p.*$', '', pub_num)  # Strip language suffix

            result = {
                "pub_num": pub_num,
                "title": doc.get("title", ""),
                "pub_type": self._infer_type(pub_num, doc.get("pubType", "")),
                "product": doc.get("product", ""),
                "url": self._build_pdf_url(
                    self._infer_type(pub_num, doc.get("pubType", "")), pub_num
                ),
            }
            results.append(result)

        return results

    def _search_html(self, query):
        """Fallback HTML scraping."""
        results = []
        try:
            url = f"https://literature.rockwellautomation.com/idc/groups/literature/documents/search?Ntt={query}"
            resp = self.session.get(url, timeout=15)
            soup = BeautifulSoup(resp.text, "html.parser")

            # Look for PDF links
            for link in soup.find_all("a", href=True):
                href = link["href"]
                if "literature/documents" in href and href.endswith(".pdf"):
                    pub_num = self._extract_pub_num(href)
                    pub_type = self._extract_pub_type(href)
                    if pub_num:
                        results.append({
                            "pub_num": pub_num,
                            "title": link.get_text(strip=True),
                            "pub_type": pub_type,
                            "url": href,
                        })
        except Exception as e:
            logger.debug(f"HTML search failed: {e}")

        return results

    def probe_catalog_prefix(self, prefix):
        """
        Probe a catalog number prefix to find all available publications.
        Tries common pub type + number combinations.
        """
        found = []
        logger.info(f"Probing catalog prefix: {prefix}")

        # Try searching for the prefix
        results = self.search(prefix, max_results=100)
        for r in results:
            if prefix.lower() in r["pub_num"].lower():
                found.append(r)
                self.discovered[r["pub_num"]] = r

        return found

    def _extract_pub_num(self, url):
        """Extract publication number from PDF URL."""
        match = re.search(r'/([^/]+)_?-en-p\.pdf', url, re.IGNORECASE)
        if match:
            return match.group(1).lower()
        return None

    def _extract_pub_type(self, url):
        """Extract publication type from URL path."""
        parts = url.split("/")
        for i, part in enumerate(parts):
            if part == "documents" and i + 1 < len(parts):
                return parts[i + 1]
        return "um"

    def _infer_type(self, pub_num, given_type=""):
        """Infer publication type from pub number or given type."""
        if given_type:
            return given_type.lower()

        # Common patterns in pub numbers
        patterns = {
            "um": ["um0", "um1", "um2", "um3", "um4", "um5"],
            "rm": ["rm0", "rm1", "rm2"],
            "pm": ["pm0", "pm1"],
            "in": ["in0", "in1", "in5"],
            "qr": ["qr0", "qr1"],
            "td": ["td0", "td1"],
        }
        for ptype, prefixes in patterns.items():
            for p in prefixes:
                if p in pub_num:
                    return ptype
        return "um"

    def _build_pdf_url(self, pub_type, pub_num):
        return (
            f"https://literature.rockwellautomation.com/idc/groups/literature/"
            f"documents/{pub_type}/{pub_num}_-en-p.pdf"
        )

    def discover_all(self, prefixes=None, delay=DELAY):
        """Sweep through catalog prefixes to discover publications."""
        prefixes = prefixes or CATALOG_PREFIXES
        all_found = []

        for i, prefix in enumerate(prefixes):
            logger.info(f"[{i+1}/{len(prefixes)}] Probing: {prefix}")
            found = self.probe_catalog_prefix(prefix)
            all_found.extend(found)
            logger.info(f"  → Found {len(found)} publications")
            time.sleep(delay)

        return all_found

    def export(self, filepath):
        """Export discovered publications to JSON."""
        output = {
            "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total": len(self.discovered),
            "publications": list(self.discovered.values()),
        }
        with open(filepath, "w") as f:
            json.dump(output, f, indent=2)
        logger.info(f"Exported {len(self.discovered)} publications to {filepath}")

    def to_python_catalog(self, filepath):
        """Generate Python catalog entries from discovered publications."""
        lines = ["# Auto-generated from scraper.py\n\nDISCOVERED_PUBLICATIONS = [\n"]
        for pub in self.discovered.values():
            lines.append(
                f'    ("{pub["pub_type"]}", "{pub["pub_num"]}"),  '
                f'# {pub.get("title", "")}\n'
            )
        lines.append("]\n")

        with open(filepath, "w") as f:
            f.writelines(lines)
        logger.info(f"Python catalog written to {filepath}")


# ── URL Prober ───────────────────────────────────────────────────────────────

def probe_url_patterns(catalog_num, session=None):
    """
    Given a catalog number like '750', probe common pub number patterns
    to find valid PDFs. Returns list of working URLs.
    """
    if session is None:
        session = requests.Session()
        session.headers.update(HEADERS)

    working = []
    num_range = range(1, 30)  # Try um001 through um029

    for ptype in PUB_TYPES:
        for n in num_range:
            pub_num = f"{catalog_num}-{ptype}{n:03d}"
            url = (
                f"https://literature.rockwellautomation.com/idc/groups/literature/"
                f"documents/{ptype}/{pub_num}_-en-p.pdf"
            )
            try:
                resp = session.head(url, timeout=10, allow_redirects=True)
                if resp.status_code == 200:
                    size = int(resp.headers.get("Content-Length", 0))
                    if size > 5000:
                        logger.info(f"  ✓ FOUND {pub_num} ({size//1024}KB)")
                        working.append({
                            "pub_num": pub_num,
                            "pub_type": ptype,
                            "url": url,
                            "size_kb": size // 1024,
                        })
                time.sleep(0.5)
            except Exception:
                pass

    return working


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        handlers=[logging.StreamHandler()],
    )

    parser = argparse.ArgumentParser(
        description="Discover Allen-Bradley publications from Rockwell Literature Library"
    )
    parser.add_argument("--search", metavar="QUERY", help="Search for publications")
    parser.add_argument("--catalog-num", metavar="NUM", help="Probe by catalog number prefix (e.g. 750)")
    parser.add_argument("--probe-urls", metavar="NUM", help="Actively probe URL patterns for a catalog number")
    parser.add_argument("--discover-all", action="store_true", help="Sweep all known catalog prefixes")
    parser.add_argument("--export", default="discovered.json", metavar="FILE", help="Export results to JSON")
    parser.add_argument("--export-python", metavar="FILE", help="Export as Python catalog entries")
    parser.add_argument("--delay", type=float, default=DELAY, help=f"Delay between requests (default: {DELAY})")

    args = parser.parse_args()

    discoverer = LiteratureDiscoverer()

    if args.search:
        results = discoverer.search(args.search)
        print(f"\nFound {len(results)} results for '{args.search}':\n")
        for r in results:
            print(f"  {r['pub_num']:<30} {r.get('title', '')[:60]}")
            print(f"    → {r['url']}")
        discoverer.discovered.update({r["pub_num"]: r for r in results})

    elif args.catalog_num:
        found = discoverer.probe_catalog_prefix(args.catalog_num)
        print(f"\nFound {len(found)} publications for prefix '{args.catalog_num}':\n")
        for r in found:
            print(f"  {r['pub_num']:<30} {r.get('title', '')[:60]}")

    elif args.probe_urls:
        print(f"\nProbing URL patterns for catalog number '{args.probe_urls}'...\n")
        session = requests.Session()
        session.headers.update(HEADERS)
        working = probe_url_patterns(args.probe_urls, session)
        print(f"\nFound {len(working)} working URLs:")
        for r in working:
            print(f"  {r['pub_num']:<30} ({r['size_kb']} KB)")
            print(f"    {r['url']}")
        discoverer.discovered.update({r["pub_num"]: r for r in working})

    elif args.discover_all:
        logger.info("Starting full discovery sweep...")
        discoverer.discover_all(delay=args.delay)
    else:
        parser.print_help()
        return

    if discoverer.discovered:
        discoverer.export(args.export)
        print(f"\nResults saved to: {args.export}")

        if args.export_python:
            discoverer.to_python_catalog(args.export_python)


if __name__ == "__main__":
    main()