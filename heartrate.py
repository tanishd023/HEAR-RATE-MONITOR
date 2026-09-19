import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks


print("Loading ECG record...")

record = wfdb.rdrecord('100', pn_dir='mitdb')

ecg = record.p_signal[:, 0]

fs = record.fs

print("Sampling frequency:", fs, "Hz")
print("Number of samples:", len(ecg))


duration = 10

samples = int(duration * fs)

ecg = ecg[:samples]

time = np.arange(len(ecg)) / fs


low_cutoff = 0.5
high_cutoff = 40

b, a = butter(
    4,
    [low_cutoff / (fs / 2),
     high_cutoff / (fs / 2)],
    btype='band'
)

filtered_ecg = filtfilt(b, a, ecg)


minimum_distance = int(0.25 * fs)

peaks, properties = find_peaks(
    filtered_ecg,
    distance=minimum_distance,
    prominence=0.3
)


rr_intervals = np.diff(peaks) / fs

average_rr = np.mean(rr_intervals)

heart_rate = 60 / average_rr

print("\n-----------------------------")
print("ECG HEART RATE RESULTS")
print("-----------------------------")

print("Number of R-peaks:", len(peaks))

print("Average RR interval:",
      round(average_rr, 3), "seconds")

print("Heart Rate:",
      round(heart_rate, 2), "BPM")

print("-----------------------------")


plt.figure(figsize=(12, 4))

plt.plot(time, ecg)

plt.xlabel("Time (seconds)")
plt.ylabel("ECG Amplitude")
plt.title("Raw ECG Signal - First 10 Seconds")

plt.grid(True)

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 4))

plt.plot(time, filtered_ecg)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Filtered ECG Signal")

plt.grid(True)

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 4))

plt.plot(
    time,
    filtered_ecg,
    label="Filtered ECG"
)

plt.plot(
    time[peaks],
    filtered_ecg[peaks],
    'ro',
    label="Detected R-peaks"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.title(
    "ECG Signal with Detected R-peaks\n"
    + "Heart Rate = "
    + str(round(heart_rate, 2))
    + " BPM"
)

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


print("\nRR Intervals:")

for i, rr in enumerate(rr_intervals):
    print(
        "Beat",
        i + 1,
        ":",
        round(rr, 3),
        "seconds"
    )

print("\nProject completed successfully!")
