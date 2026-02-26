# Exoplanet Mass Prediction & OOD Analysis

## Overview

This project explores the prediction of exoplanet mass using orbital and stellar parameters, with a focus on out-of-distribution (OOD) generalization.

The current stage focuses on exploratory data analysis and spatial visualization of confirmed exoplanet host systems using data from the NASA Exoplanet Archive.

Feature analysis and modeling are currently in progress.

---

## Current Progress

### 1. 3D Galactic Visualization

Using galactic coordinates (`glon`, `glat`) and system distance (`sy_dist`), host stars are projected into 3D Cartesian space:

x = d cos(b) cos(l)  
y = d cos(b) sin(l)  
z = d sin(b)

This allows visualization of the spatial distribution of known exoplanet systems relative to the Sun.

### Observed Structures

Two prominent directed beams appear in the visualization:

- **Kepler field**  
  A dense conical structure corresponding to the fixed deep-field survey conducted by the Kepler mission toward the Cygnus and Lyra constellations.

- **Microlensing surveys**  
  A long, narrow beam directed toward the Galactic bulge, produced by microlensing surveys such as MOA, OGLE, KMTNet, and HST (when used for follow-ups).

---

## Project Goals

The long-term goal is to:

- Predict exoplanet mass from orbital and stellar parameters  
- Analyze robustness under distribution shift  
- Study OOD performance across:
  - Single vs multi-star systems  
  - Generalization over Huge Mass Planets
  - Different stellar populations  

---

## Data

Data is sourced from the [NASA Exoplanet Archive](!https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars).

---

## Next Steps

- Feature correlation analysis  
- Feature importance exploration  
- Construction of baseline models  
- Explore and define OOD splits  
- Performance comparison across distribution regimes  

---

## Status

Active development.  
Visualization complete.  
Feature analysis in progress.