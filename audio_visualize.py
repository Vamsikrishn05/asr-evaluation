import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load audio
wav_file = "single_s1_22032_11908.wav"
y, sr = librosa.load(wav_file, sr=None)

# Plot waveform
plt.figure(figsize=(12, 3))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.tight_layout()
plt.show()

# Compute STFT
stft = np.abs(librosa.stft(y))
db = librosa.amplitude_to_db(stft, ref=np.max)

plt.figure(figsize=(12, 4))
librosa.display.specshow(db, sr=sr, x_axis="time", y_axis="hz")
plt.title("Spectrogram (dB scale)")
plt.colorbar()
plt.tight_layout()
plt.show()

# Compute RMS energy (frame energy)
rms = librosa.feature.rms(y=y)[0]
times = librosa.frames_to_time(np.arange(len(rms)), sr=sr)

plt.figure(figsize=(12, 3))
plt.plot(times, rms)
plt.title("RMS Energy Curve")
plt.xlabel("Time (s)")
plt.tight_layout()
plt.show()
