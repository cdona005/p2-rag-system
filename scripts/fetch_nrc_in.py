"""Download NRC Information Notices (PDF) for a range of years into a raw folder outside the repo.

Usage (from the repo root):
    uv run python scripts/fetch_nrc_in.py 1995 2004 --out ../p2-raw/nrc-in

Each year page at nrc.gov lists links such as /docs/ML0310/ML031060175.pdf. The files are saved as
<out>/<ML0310>/<ML031060175.pdf>, one folder per NRC folder prefix, so that `p2 ingest` can be run once
per folder with a --source that names that folder (the manifest then records each file's own address).
Files already downloaded are skipped, and there is a pause between requests to be polite to the server.
"""

from __future__ import annotations

import argparse
import re
import sys
import subprocess
import time
from pathlib import Path

BASE = "https://www.nrc.gov"
YEAR_URL = BASE + "/documents-reports/generic-communications/information-notices/{year}"
DOC_LINK = re.compile(r'href="(/docs/(ML\d+)/(ML\d+\.pdf))"')
PAUSE_S = 0.5


def get(url: str) -> bytes:
    """Fetch a URL with curl and return the body (nrc.gov refuses Python's urllib with a 403, and serves curl)."""
    done = subprocess.run(["curl", "-sS", "-f", "-L", "-m", "60", url], capture_output=True)
    if done.returncode != 0:
        raise OSError(f"curl failed for {url}: {done.stderr.decode(errors='replace').strip()}")
    return done.stdout


def year_links(year: int) -> list[tuple[str, str, str]]:
    """The (path, folder, file name) of every PDF linked from one year's page, without repeats."""
    page = get(YEAR_URL.format(year=year)).decode("utf-8", errors="replace")
    return list(dict.fromkeys(DOC_LINK.findall(page)))


def main() -> int:
    """Download every notice of the years given on the command line."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("first", type=int, help="first year")
    parser.add_argument("last", type=int, help="last year (inclusive)")
    parser.add_argument("--out", default="../p2-raw/nrc-in", help="folder for the raw PDFs")
    args = parser.parse_args()
    out = Path(args.out)
    total = new = 0
    for year in range(args.first, args.last + 1):
        links = year_links(year)
        print(f"{year}: {len(links)} links", flush=True)
        for path, folder, name in links:
            total += 1
            target = out / folder / name
            if target.exists():
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                target.write_bytes(get(BASE + path))
            except OSError as error:
                print(f"  failed {path}: {error}", file=sys.stderr)
                continue
            new += 1
            time.sleep(PAUSE_S)
    print(f"{total} links, {new} downloaded into {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
