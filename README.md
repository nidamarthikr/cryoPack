# cryoPack

cryoPack
cryoPack is a work‑in‑progress package that provides tools for model evaluation and quality assessment of cryo‑EM maps and projection datasets. The package focuses on reference‑free, statistically grounded diagnostics that help assess data quality prior to and after 3D reconstruction.

Package Overview
The qcheck module currently contains two programs:
1. cP_qcheck.mqa (Map Quality Assessment)
This program evaluates phase-related properties of a reconstructed cryo‑EM 3D map and computes statistical parameters to assess map quality.
It is particularly useful for:

Quantitative assessment of map integrity
Detecting the presence of non‑particle contributions in the reconstruction

Inputs:

Cryo‑EM map file (.mrc or .map)
Contour level

The contour value is used to generate a mask for subsequent calculations.

2. cP_qcheck.poa (Projection Orientation Assessment)
This program evaluates the orientation assignment and alignment of projections used for reconstruction in a reference‑free manner.
It provides:

Assessment of orientation consistency
Evaluation of angular ordering
Estimation of dataset completeness based on effective sampling
Detection of misalignment or heterogeneity

The analysis is based on:

Lag‑1 autocorrelation (AC)
Global Score (GS), which combines intrinsic ordering with effective sampling


Input Format

cP_qcheck.mqa accepts:

Cryo‑EM map (.mrc / .map)


cP_qcheck.poa accepts:

Projection images in HDF format (.hdf)


Usage

cP.qcheck_mqa inputfile.mrc 1.5

cP.qcheck_poa inputfile.hdf 2

Help

cP.qcheck_mqa -h
cP.qcheck_poa -h


The details for one of the function is publised as a preprint in biorxiv.

Please follow the link to the paper. "https://www.biorxiv.org/content/10.1101/2022.12.31.521834v1"

Changes will be made to the up comming versions and accompied with paper published. 
