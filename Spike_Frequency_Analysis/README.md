# Spike Frequency Analysis

This folder contains reproducible Python workflows for detecting spontaneous action potentials and calculating spike frequency from current-clamp electrophysiological recordings.

The workflow is designed for patch-clamp recordings exported as HEKA/PatchMaster ASCII files.

## Contents

- `spike_frequency_workflow.py`  
  Reusable Python script for spike-frequency analysis.

- `spike_frequency_publication_workflow.ipynb`  
  Publication-style notebook including explanation, analysis workflow, export tables, and representative quality-control visualization.

## Workflow

The analysis includes:

1. Import of HEKA/PatchMaster ASCII recordings
2. Detection of action potential peaks
3. Calculation of spike count
4. Calculation of spike frequency in Hz
5. Export of summary tables for downstream statistical analysis
6. Representative quality-control visualization of detected spikes

Recording names and experimental conditions are anonymized in this public version to protect unpublished experimental details.
