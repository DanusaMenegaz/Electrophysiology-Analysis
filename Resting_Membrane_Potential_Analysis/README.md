# Resting Membrane Potential Analysis

This folder contains reproducible Python workflows for extracting resting membrane potential (RMP) values from current-clamp electrophysiological recordings.

The workflow is designed for patch-clamp recordings exported as HEKA/PatchMaster ASCII files.

## Contents

- `rmp_publication_workflow.ipynb`  
  Publication-style notebook including explanation, analysis workflow, export tables, and representative quality-control visualization.

## Workflow

The analysis includes:

1. Import of HEKA/PatchMaster ASCII recordings
2. Selection of a baseline window
3. Calculation of RMP mean in mV
4. Calculation of RMP median in mV
5. Estimation of baseline SD/noise
6. Export of summary tables for downstream statistical analysis
7. Representative quality-control visualization of the RMP baseline window and full recording

Both mean and median RMP values are reported. The median RMP is preferred for downstream statistical analysis because it is less sensitive to spikes, transient depolarizations, and outliers within the baseline window.

Recording names and experimental conditions are anonymized in this public version to protect unpublished experimental details.
