# TPC1 Single-Channel Analysis

This folder contains a reproducible Python workflow for quantitative analysis of TPC1 single-channel electrophysiological recordings exported from HEKA PatchMaster ASCII files.

The analysis pipeline was developed for publication-related processing of excised-patch single-channel recordings associated with the manuscript.

## Contents

- `TPC1_single_channel_publication_code.ipynb`  
  Main Jupyter/Colab notebook containing the full analysis workflow.

## Analysis workflow

The notebook includes:

1. Import of Python libraries
2. User-defined recording settings
3. HEKA ASCII file import
4. Single-channel state classification
5. Open probability (Po) calculation
6. Single-channel amplitude quantification
7. Batch analysis of multiple recordings
8. Export of results tables
9. Representative quality-control visualization

## Main outputs

The pipeline calculates:

- Open probability (Po)
- Single-channel amplitude in pA
- Closed and open current levels
- Threshold used for state classification
- Quality-control plots for representative recordings

## Software

The workflow was implemented in Python using standard scientific libraries including:

- NumPy
- Pandas
- SciPy
- Matplotlib

## Notes

Raw electrophysiology recordings are not included in this repository. The notebook is intended to document the computational workflow used for analysis of HEKA PatchMaster ASCII exports.

Representative quality-control figures are used to illustrate the analysis logic and are not intended to reproduce the exact visual scaling of assembled publication panels.
