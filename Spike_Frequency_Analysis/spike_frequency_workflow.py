# ============================================================
# Spike Frequency Analysis Workflow
# ============================================================
#
# Purpose:
# This workflow detects spontaneous action potentials from
# current-clamp electrophysiology recordings and calculates
# spike frequency in Hz.
#
# Designed for HEKA/PatchMaster ASCII exports.
#
# Public version:
# - Recording names are anonymized
# - Experimental group names are generic
# - No confidential mutant, drug, or project information is included
#
# Outputs:
# - Spike-frequency summary table
# - Spike-by-spike table
# - Quality-control plot showing detected spikes
# - GraphPad-friendly spike-frequency table
#
# ============================================================


# ------------------------------------------------------------
# 1. Import libraries
# ------------------------------------------------------------

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# ------------------------------------------------------------
# 2. User settings
# ------------------------------------------------------------

# Folder containing HEKA/PatchMaster ASCII files
# Example for Google Colab:
# base_path = "/content/drive/MyDrive/PatchClampData/Python2/"
base_path = "/content/drive/MyDrive/PatchClampData/Python2/"


# Generic experimental group name
condition_name = "Example_Group"


# Anonymized recording names
file_names = [
    "recording_01.asc",
    "recording_02.asc",
    "recording_03.asc",
]


# Analysis window
start_time = 0.3
end_time = 60


# Spike-detection parameters
min_peak_mV = 0
min_prominence_mV = 20
refractory_period = 0.05


# Plot settings
y_min = -90
y_max = 50


# Output settings
save_figures = True
output_folder = "spike_frequency_output"


# ------------------------------------------------------------
# 3. Prepare output folder
# ------------------------------------------------------------

os.makedirs(output_folder, exist_ok=True)


# ------------------------------------------------------------
# 4. Load HEKA/PatchMaster ASCII file
# ------------------------------------------------------------

def load_heka_asc(file_path):
    """
    Load a HEKA/PatchMaster ASCII file.

    Expected columns include:
    - Index
    - Time[s]
    - V-mon[V]
    - Stimulus

    Returns:
    pandas DataFrame with:
    - Time_s
    - Voltage_mV
    """

    header_line = None

    with open(file_path, "r") as f:
        for i, line in enumerate(f):
            if line.strip().startswith('"Index"') or line.strip().startswith("Index"):
                header_line = i
                break

    if header_line is None:
        raise ValueError("Could not find the header line starting with Index.")

    data = pd.read_csv(
        file_path,
        sep=",",
        skiprows=header_line
    )

    data.columns = (
        data.columns
        .str.strip()
        .str.replace('"', '', regex=False)
    )

    time_col = [col for col in data.columns if "Time[s]" in col][0]
    voltage_col = [col for col in data.columns if "V-mon[V]" in col][0]

    data = data[[time_col, voltage_col]].copy()
    data.columns = ["Time_s", "Voltage_V"]

    data["Time_s"] = pd.to_numeric(data["Time_s"], errors="coerce")
    data["Voltage_V"] = pd.to_numeric(data["Voltage_V"], errors="coerce")

    data = data.dropna()

    data["Voltage_mV"] = data["Voltage_V"] * 1000

    return data[["Time_s", "Voltage_mV"]]


# ------------------------------------------------------------
# 5. Analyze spike frequency from one recording
# ------------------------------------------------------------

def analyze_spike_frequency(
    file_path,
    recording_name,
    start_time=0.3,
    end_time=60,
    min_peak_mV=0,
    min_prominence_mV=20,
    refractory_period=0.05,
    y_min=-90,
    y_max=50,
    save_figures=True
):
    """
    Detect spontaneous action potentials and calculate spike frequency.

    Returns:
    - summary dictionary
    - spike-by-spike table
    """

    data = load_heka_asc(file_path)

    analysis_data = data[
        (data["Time_s"] >= start_time) &
        (data["Time_s"] <= end_time)
    ].copy()

    time = analysis_data["Time_s"].values
    voltage = analysis_data["Voltage_mV"].values

    if len(time) < 10:
        raise ValueError("Selected analysis window is too short or empty.")

    dt = np.median(np.diff(time))
    sampling_rate = 1 / dt
    min_distance_points = int(refractory_period / dt)

    peaks, properties = find_peaks(
        voltage,
        height=min_peak_mV,
        prominence=min_prominence_mV,
        distance=min_distance_points
    )

    spike_times = time[peaks]
    spike_peaks_mV = voltage[peaks]

    spike_count = len(peaks)
    duration_s = time[-1] - time[0]
    spike_frequency_Hz = spike_count / duration_s

    print(f"\nAnalysis complete: {recording_name}")
    print(f"Analysis window: {start_time:.2f} to {end_time:.2f} s")
    print(f"Duration analyzed: {duration_s:.2f} s")
    print(f"Sampling rate: {sampling_rate:.1f} Hz")
    print(f"Spike count: {spike_count}")
    print(f"Spike frequency: {spike_frequency_Hz:.3f} Hz")

    # Quality-control plot
    plt.figure(figsize=(15, 5), dpi=300)

    plt.plot(
        time,
        voltage,
        color="black",
        linewidth=0.8
    )

    plt.scatter(
        spike_times,
        spike_peaks_mV,
        color="red",
        s=25,
        label="Detected spikes"
    )

    plt.xlabel("Time (s)", fontsize=14)
    plt.ylabel("Membrane Potential (mV)", fontsize=14)
    plt.title(f"{recording_name} - Spike Detection", fontsize=14)

    plt.xlim(start_time, end_time)
    plt.ylim(y_min, y_max)
    plt.legend(frameon=False)
    plt.tight_layout()

    if save_figures:
        figure_path_png = os.path.join(
            output_folder,
            f"{recording_name}_spike_detection.png"
        )

        figure_path_svg = os.path.join(
            output_folder,
            f"{recording_name}_spike_detection.svg"
        )

        plt.savefig(figure_path_png, dpi=600, bbox_inches="tight")
        plt.savefig(figure_path_svg, format="svg", bbox_inches="tight")

    plt.show()

    spike_table = pd.DataFrame({
        "recording_name": recording_name,
        "spike_number": np.arange(1, spike_count + 1),
        "spike_time_s": spike_times,
        "spike_peak_mV": spike_peaks_mV
    })

    summary = {
        "recording_name": recording_name,
        "condition": condition_name,
        "start_time_s": start_time,
        "end_time_s": end_time,
        "duration_s": duration_s,
        "sampling_rate_Hz": sampling_rate,
        "spike_count": spike_count,
        "spike_frequency_Hz": spike_frequency_Hz,
        "min_peak_mV": min_peak_mV,
        "min_prominence_mV": min_prominence_mV,
        "refractory_period_s": refractory_period
    }

    return summary, spike_table


# ------------------------------------------------------------
# 6. Run batch analysis
# ------------------------------------------------------------

all_results = []
all_spike_tables = []

file_paths = [os.path.join(base_path, file_name) for file_name in file_names]

print(f"Condition: {condition_name}")
print(f"Number of recordings listed: {len(file_paths)}")


for i, file_path in enumerate(file_paths, start=1):

    recording_name = f"recording_{i:02d}"

    print("\n----------------------------------------")
    print(f"Analyzing: {recording_name}")

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue

    try:
        summary, spike_table = analyze_spike_frequency(
            file_path=file_path,
            recording_name=recording_name,
            start_time=start_time,
            end_time=end_time,
            min_peak_mV=min_peak_mV,
            min_prominence_mV=min_prominence_mV,
            refractory_period=refractory_period,
            y_min=y_min,
            y_max=y_max,
            save_figures=save_figures
        )

        all_results.append(summary)
        all_spike_tables.append(spike_table)

    except Exception as error:
        print(f"Error analyzing {recording_name}: {error}")


# ------------------------------------------------------------
# 7. Create and save summary table
# ------------------------------------------------------------

summary_df = pd.DataFrame(all_results)

if len(summary_df) > 0:

    summary_df = summary_df[[
        "recording_name",
        "condition",
        "spike_count",
        "duration_s",
        "spike_frequency_Hz",
        "sampling_rate_Hz",
        "min_peak_mV",
        "min_prominence_mV",
        "refractory_period_s"
    ]].copy()

    summary_df["duration_s"] = summary_df["duration_s"].round(2)
    summary_df["spike_frequency_Hz"] = summary_df["spike_frequency_Hz"].round(3)
    summary_df["sampling_rate_Hz"] = summary_df["sampling_rate_Hz"].round(1)

    print("\nSpike-frequency summary table:")
    print(summary_df)

    summary_output_path = os.path.join(
        output_folder,
        "spike_frequency_summary.csv"
    )

    summary_df.to_csv(summary_output_path, index=False)

    print(f"\nSaved summary table: {summary_output_path}")


# ------------------------------------------------------------
# 8. Create and save spike-by-spike table
# ------------------------------------------------------------

if len(all_spike_tables) > 0:

    spike_by_spike_df = pd.concat(all_spike_tables, ignore_index=True)

    spike_by_spike_df["spike_time_s"] = spike_by_spike_df["spike_time_s"].round(4)
    spike_by_spike_df["spike_peak_mV"] = spike_by_spike_df["spike_peak_mV"].round(2)

    print("\nSpike-by-spike table:")
    print(spike_by_spike_df)

    spike_table_output_path = os.path.join(
        output_folder,
        "spike_by_spike_table.csv"
    )

    spike_by_spike_df.to_csv(spike_table_output_path, index=False)

    print(f"\nSaved spike-by-spike table: {spike_table_output_path}")


# ------------------------------------------------------------
# 9. GraphPad-friendly output
# ------------------------------------------------------------

if len(summary_df) > 0:

    graphpad_df = summary_df[["spike_frequency_Hz"]].copy()
    graphpad_df.columns = [condition_name]

    graphpad_output_path = os.path.join(
        output_folder,
        "graphpad_spike_frequency_Hz.csv"
    )

    graphpad_df.to_csv(graphpad_output_path, index=False)

    print(f"\nSaved GraphPad-friendly table: {graphpad_output_path}")


# ------------------------------------------------------------
# 10. Final message
# ------------------------------------------------------------

print("\nSpike-frequency analysis finished.")
