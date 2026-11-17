# Progress log

## Session 1 — 2026-11-17 (setup + fire history EDA) ✅
**Done**
- Installed Git and Miniforge (conda, conda-forge channel); created conda env `firerisk` (Python 3.11)
  with all packages from `environment.yml`
- Fixed GDAL warning (`GDAL_DATA` not defined) with
  `conda env config vars set GDAL_DATA="$env:CONDA_PREFIX\Library\share\gdal"`
- Fixed Jupyter kernel crash (Windows DLL conflict, exit code 0xC06D007F): launch VS Code from the
  activated env (`conda activate firerisk` → `code .`) so the kernel inherits the env's PATH
- Project structure, `.gitignore`, `README.md`, `CLAUDE.md`; repo on GitHub:
  https://github.com/fivosgk/wildfire-risk-predictor
- `src/download_firms.py`: downloads yearly NASA FIRMS VIIRS S-NPP detections for Greece (no API key needed)
- `notebooks/01_fire_history_eda.ipynb`: cleaning (vegetation fires, no low confidence), fires per year
  and month, density map, per-region comparison
- Basemap: switched from CARTO (needs API key since Sept 2026) to `cx.providers.Esri.WorldGrayCanvas`

**Key findings**
- Detections ≠ fires: one large fire produces hundreds of detections → compare regions by *fire days*
- Agricultural burning pollutes the labels: Kentriki/Dytiki Makedonia have only 17% / 33% of detections
  in summer; Thessalia's summer peak overlaps with wheat-stubble burning
- Stereá Elláda (Evia 2021) and Anatoliki Makedonia-Thraki (Evros 2023) depend on one extreme year
  (~46-47% of detections), which would distort a year-based train/test split

**Decision: study area = Attica (Attiki)**
- Cleanest wildfire signal: 85% of detections in summer (Jun–Sep)
- ~368 summer fire days over the period, not dominated by a single year (biggest year = 30%)
- Small area (~3,800 km²) → fast satellite/weather downloads
- Well-known recent fires (Mati 2018, Varympompi 2021, Fyli 2023, Varnavas 2024)
- Known caveat: large urban area → filter to forest/shrubland with land-cover data in Session 2

**Next — Session 2**
- Attica boundary + regular grid of cells (decide cell size, e.g. 1 km)
- Land cover (CORINE) to keep only forest/shrub/natural vegetation cells
- Fire label per cell and time period from FIRMS
- Features per cell: vegetation (NDVI / moisture from Sentinel-2 or MODIS), weather (Open-Meteo),
  elevation & slope
