# TPC1 Single-Channel Analysis

This folder contains a reproducible Python workflow for quantitative analysis of lysosomal TPC1 single-channel electrophysiological recordings exported from HEKA PatchMaster ASCII files.

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

## Associated Publication

This single-channel analysis workflow was used for electrophysiological analysis associated with the following publication:

Deutsch R, Jörs S, Klingl Y, Kudrina V, Menegaz D, Jaślan D, Serianz Z, Vogel A, Abrahamian C, Bhunia S, Tavhelidse-Suck T, Richter C, Wirth A, Urban N, Northoff B, Wilfert W, Klugbauer N, Bracher F, Keller M, Geisler F, Schaefer M, Teupser D, Holdt L, Belkaya S, Freichel M, Grimm C.  
**TPC1-dependent control of endosomal pH and transferrin uptake determines cellular iron status.**  
*Proceedings of the National Academy of Sciences of the United States of America.* 2026;123(32):e2602941123.  
doi: 10.1073/pnas.2602941123

The repository provides the Python-based workflow used for representative single-channel current visualization, amplitude estimation, open-probability analysis, and quality-control plotting.
