# Project context for Claude

## Goal
Portfolio data science project (GitHub + CV) for Data Scientist job applications:
predict wildfire risk per grid cell in a region of Greece from satellite, weather and terrain data.

## Decisions so far
- Study area: **Attica (Attiki)**: cleanest summer wildfire signal, not dominated by one year,
  small enough for fast downloads (see notebooks/01 and PROGRESS.md for the reasoning)
- Fire labels: NASA FIRMS VIIRS S-NPP (375 m), 2012 onwards, vegetation fires (type 0),
  low-confidence detections dropped
- Basemaps: `cx.providers.Esri.WorldGrayCanvas` (CARTO now requires an API key)
- On Windows, start VS Code from the activated env (`conda activate firerisk` then `code .`),
  otherwise the Jupyter kernel crashes on GDAL DLLs

## About the user
Mathematician, Decisioning Consultant (Pega CDH), doing an MSc in Data Science & ML.
Knows basic Python and SQL. Works in ~2-hour sessions.

## Plan
- Session 1: setup (repo, env, structure), choose study area, NASA FIRMS historical fires, EDA with maps
- Session 2: satellite data (Sentinel-2/MODIS: NDVI, vegetation moisture), weather (Open-Meteo),
  elevation/slope, build dataset per grid cell
- Session 3: modelling: logistic regression baseline, then Random Forest / XGBoost, ROC-AUC,
  feature importance, train/test split by year
- Session 4 (optional): CNN on satellite images
- Wrap-up: risk map, README with results, CV bullet

## How to work
- Respond to the user in Greek; code, comments and repo docs in English.
- Explain what each step does and why, so the user can defend it in an interview.
- Code must be clean, commented and GitHub-ready.
- At the end of each session, update PROGRESS.md with where we stopped and next steps.

## Conventions
- Environment: conda (Miniforge), env name `firerisk`, defined in `environment.yml`
  (conda-forge only). Add new packages to environment.yml, then
  `conda env update -f environment.yml --prune`.
- Raw/processed data live in `data/` and are NOT committed. API keys go in `.env` (not committed).
- Notebooks are numbered: `01_...ipynb`, `02_...ipynb`. Reusable logic goes in `src/`.
