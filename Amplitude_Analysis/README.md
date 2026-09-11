# Action Potential Amplitude Analysis

This folder contains a reproducible Python workflow for extracting action-potential amplitude values from current-clamp electrophysiological recordings.

The workflow is designed for patch-clamp recordings exported as HEKA/PatchMaster ASCII files.

## Contents

- `amplitude_publication_workflow.ipynb`  
  Publication-style notebook including explanation, analysis workflow, export tables, and representative quality-control visualization.

## Workflow

The analysis includes:

1. Import of HEKA/PatchMaster ASCII recordings
2. Detection of action-potential peaks
3. Estimation of local membrane potential baseline before each action potential
4. Calculation of action-potential amplitude in mV
5. Export of summary and spike-by-spike tables
6. Representative quality-control visualization of detected peaks and local baselines

The primary amplitude metric is calculated as:

**AP amplitude = AP peak − median local membrane potential 20–5 ms before the AP peak**

Recording names and experimental conditions are anonymized in this public version to protect unpublished experimental details.
