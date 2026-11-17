"""
Download yearly NASA FIRMS active-fire detections for Greece.

Source
------
FIRMS "yearly summary by country" CSV files:
    https://firms.modaps.eosdis.nasa.gov/country/

Each row is one *fire detection*: a satellite pixel that was significantly
hotter than its surroundings at the moment the satellite passed over.

We use VIIRS S-NPP (375 m pixels, available since 2012). It detects smaller
fires than the older MODIS sensor (1 km pixels), which matters in Greece where
many fires are small.

Usage (from the project root, with the `firerisk` env active):
    python -m src.download_firms
"""

from pathlib import Path

import requests
from tqdm import tqdm

# --- Settings -----------------------------------------------------------------
SENSOR = "viirs-snpp"
COUNTRY = "Greece"
YEARS = range(2012, 2026)  # 2012..2025; years not yet published are skipped

# URL pattern of the FIRMS country files, e.g.
# .../data/country/viirs-snpp/2023/viirs-snpp_2023_Greece.csv
URL_TEMPLATE = (
    "https://firms.modaps.eosdis.nasa.gov/data/country/"
    "{sensor}/{year}/{sensor}_{year}_{country}.csv"
)

# Files are saved in <project root>/data/raw/firms/ (ignored by Git)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw" / "firms"


def download_year(year: int) -> Path | None:
    """Download one year of detections. Returns the file path, or None if unavailable."""
    out_path = RAW_DIR / f"{SENSOR}_{year}_{COUNTRY}.csv"

    # Skip files we already have, so the script can be re-run safely
    if out_path.exists():
        print(f"{year}: already downloaded, skipping")
        return out_path

    url = URL_TEMPLATE.format(sensor=SENSOR, year=year, country=COUNTRY)
    response = requests.get(url, timeout=60)

    if response.status_code == 404:
        print(f"{year}: not available on FIRMS (404), skipping")
        return None
    response.raise_for_status()  # stop on any other HTTP error

    out_path.write_bytes(response.content)
    print(f"{year}: saved {out_path.name} ({len(response.content) / 1e6:.1f} MB)")
    return out_path


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    downloaded = [download_year(year) for year in tqdm(YEARS, desc="Years")]
    n_ok = sum(path is not None for path in downloaded)
    print(f"\nDone: {n_ok}/{len(YEARS)} years available in {RAW_DIR}")


if __name__ == "__main__":
    main()
