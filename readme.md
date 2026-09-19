# ECG Heart Rate Detection Using Python

## About the Project

This project is a Digital Signal Processing (DSP) based ECG Heart Rate Detection system developed using Python.

An Electrocardiogram (ECG) is a signal that represents the electrical activity of the heart. The aim of this project is to process an ECG signal, identify the important R-peaks, and calculate the heart rate in Beats Per Minute (BPM).

The project uses a real ECG signal from the MIT-BIH Arrhythmia Database and processes it using Python.

## How It Works

The ECG signal goes through the following stages:

ECG Dataset → Signal Filtering → R-Peak Detection → RR Interval Calculation → Heart Rate

### 1. ECG Signal Acquisition

The ECG signal is obtained from the MIT-BIH Arrhythmia Database using the WFDB Python library.

The selected ECG record is sampled at 360 Hz, meaning that 360 samples of the signal are recorded every second.

### 2. Signal Filtering

The raw ECG signal may contain unwanted noise and baseline variations.

A Butterworth Band-Pass Filter is applied to the signal with a frequency range of approximately 0.5 Hz to 40 Hz.

This helps retain the important components of the ECG signal while reducing unwanted frequency components.

### 3. R-Peak Detection

The R-wave is one of the most prominent features of an ECG signal.

After filtering, the `find_peaks()` function from SciPy is used to detect the R-peaks automatically.

Each detected R-peak represents an estimated heartbeat.

### 4. RR Interval Calculation

The time difference between two consecutive R-peaks is called the RR interval.

The RR interval is calculated from the detected peak positions and the sampling frequency.

### 5. Heart Rate Calculation

The heart rate is calculated using the average RR interval.

Heart Rate (BPM) = 60 / Average RR Interval

For example, if the average RR interval is 0.8 seconds:

Heart Rate = 60 / 0.8 = 75 BPM

## Technologies Used

- Python
- WFDB
- NumPy
- SciPy
- Matplotlib

## Signal Processing Concepts Used

- Sampling
- Digital Signal Processing
- Band-Pass Filtering
- Butterworth Filter
- Noise Reduction
- Peak Detection
- R-Peak Detection
- RR Interval Analysis
- Heart Rate Estimation
- Signal Visualization

## Output

The program displays:

- Raw ECG waveform
- Filtered ECG waveform
- Detected R-peaks
- Number of detected heartbeats
- Average RR interval
- Estimated heart rate in BPM

## Project Flow

```text
        ECG Dataset
             ↓
       Raw ECG Signal
             ↓
      Band-Pass Filter
             ↓
       Filtered ECG
             ↓
       R-Peak Detection
             ↓
       RR Interval
             ↓
      Heart Rate (BPM)
