# Electrophysiology-Analysis

## Electrophysiology Analysis Repository

This repository contains reproducible Python workflows for the quantitative analysis of electrophysiological recordings obtained using patch-clamp techniques.

The primary workflow includes analysis of TPC1 single-channel recordings exported from HEKA PatchMaster ASCII files, including:

* Channel-state classification
* Open probability (Po) calculation
* Single-channel amplitude quantification
* Batch processing of recordings
* Quality-control visualization
* Export of publication-ready results

Additional scripts for electrophysiological analyses, including resting membrane potential (RMP), spike frequency, amplitude measurements, and statistical analysis, are also provided.

All code is publicly available and maintained by the authors in accordance with PNAS code availability requirements.

---

## Features

* **TPC1 Single-Channel Analysis**: Quantification of channel activity from HEKA PatchMaster ASCII files.
* **Open Probability (Po) Analysis**: Calculation of channel open probability.
* **Single-Channel Amplitude Quantification**: Measurement of current amplitudes.
* **Quality-Control Visualization**: Representative trace visualization and workflow validation.
* **Batch Processing**: Automated analysis of multiple recordings.
* **Resting Membrane Potential (RMP) Analysis**: Calculate and visualize RMP.
* **Spike Frequency Analysis**: Determine spontaneous action potential frequencies.
* **Amplitude Calculation**: Measure action potential amplitudes within specified voltage ranges.
* **Statistical Analysis**: Perform ANOVA and descriptive statistics.
* **Baseline Adjustment**: Normalize baseline for amplitude analysis.

---

## Repository Structure

### Main publication workflow

* `Single_Channel_Analysis/TPC1_single_channel_publication_code.ipynb`

  * Reproducible workflow used for TPC1 single-channel analysis associated with the PNAS manuscript.

### Additional electrophysiology scripts

* `Amplitude (mV).py`
* `Spike Frequency (Hz).py`
* `Resting Membrane Potential (mV).py`
* `statistics_amplitude.py`
* `statistics_rmp.py`
* `statistics_spike_frequency.py`
* `anova_statistics.py`

---

## Requirements

* **Python 3.8+**
* Required libraries: `numpy`, `pandas`, `matplotlib`, `scipy`

Install dependencies:

```bash
pip install numpy pandas matplotlib scipy
```

## Usage

### TPC1 Single-Channel Analysis

Open and run:

```text
Single_Channel_Analysis/TPC1_single_channel_publication_code.ipynb
```

This notebook contains the complete workflow for:

* Channel-state classification
* Open probability (Po) calculation
* Single-channel amplitude quantification
* Batch analysis of recordings
* Quality-control visualization
* Export of publication-ready results

### Additional scripts

```bash
python "Amplitude (mV).py"
python "Spike Frequency (Hz).py"
```

---

## Example Output

The repository generates publication-quality outputs including:

* Open probability (Po) measurements
* Single-channel amplitude quantification
* Quality-control trace visualizations
* Statistical summaries
* Publication-ready figures and tables

---

## Citation

If you use this repository, please cite:

Menegaz, D. *Electrophysiology-Analysis*. GitHub Repository.

Repository:
https://github.com/DanusaMenegaz/Electrophysiology-Analysis

---

## About the Author

This repository was created and is maintained by Danusa Menegaz, PhD, an electrophysiologist specializing in patch-clamp techniques with extensive experience in ion channel physiology, single-channel electrophysiology, and quantitative data analysis.

---

## Reproducibility and Code Availability

This repository contains the code used for electrophysiological analyses associated with the manuscript.

The analysis workflow includes:

* Data import from HEKA PatchMaster ASCII files
* Signal processing and baseline correction
* TPC1 single-channel electrophysiology analysis
* Open probability (Po) calculation
* Single-channel amplitude quantification
* Resting membrane potential (RMP) analysis
* Spike frequency analysis
* Statistical analysis
* Quality-control visualization

All code is publicly available and maintained by the authors in accordance with PNAS data and code availability requirements.

---

## Professional Training

### MasterSchool Data Analytics School (2024)

Completed a 1440-hour professional training program in Data Analytics and Data Science.

Skills acquired:

* Python Programming
* SQL and Advanced SQL
* Tableau
* Data Visualization
* Data Wrangling
* Machine Learning Fundamentals
* Data Storytelling

Certificates available in this repository:

* Data Science Fundamentals (English)
* Data Science Fundamentals (German)
