# Wildfire Risk Predictor

Predicting wildfire risk per grid cell in a region of Greece, using historical fire detections (NASA FIRMS), satellite vegetation indices (Sentinel-2 / MODIS), weather (Open-Meteo) and terrain data.

> 🚧 Work in progress

## Project structure

```
├── data/
│   ├── raw/            # downloaded source data (not tracked by Git)
│   └── processed/      # cleaned, model-ready datasets (not tracked by Git)
├── notebooks/          # exploration & analysis, numbered in order
├── src/                # reusable Python code (download, features, modelling)
├── outputs/
│   └── figures/        # maps and plots used in this README
├── environment.yml     # conda environment specification
└── README.md
```

## Setup

```bash
conda env create -f environment.yml
conda activate firerisk
```

## Roadmap

- [ ] Study area selection & historical fire data (NASA FIRMS), EDA with maps
- [ ] Feature engineering: vegetation indices, weather, elevation/slope per grid cell
- [ ] Modelling: logistic regression baseline → Random Forest / XGBoost, year-based train/test split
- [ ] (Optional) CNN on satellite imagery
- [ ] Final risk map & results
