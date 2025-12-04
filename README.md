# ASR Evaluation and Audio Analysis – SPIRE Lab

This repository contains Python scripts, evaluation outputs, signal-processing plots, and a written analysis comparing two Automatic Speech Recognition (ASR) systems using WER (Word Error Rate) and CER (Character Error Rate). The project also includes spectrogram, waveform, and RMS energy analysis of the speech audio.

## 1. How the Code Works

### 1.1 ASR Evaluation Script (`evaluate_asr.py`)

This script performs transcript accuracy measurement for two ASR outputs.

Processing steps:
- Reads the input TSV files, which contain:
  - segment start time
  - segment end time
  - ASR system output
  - human reference transcript
- Normalises text by converting it to lowercase and removing extra spaces.
- Uses the `jiwer` alignment library to compute:
  - sentence-level WER (Word Error Rate)
  - sentence-level CER (Character Error Rate)
- Joins the full transcript and computes:
  - overall corpus WER
  - overall corpus CER
- Stores results in CSV files and prints the final evaluation scores.

This allows direct comparison between ASR system outputs.

### 1.2 Audio Analysis Script (`audio_visualize.py`)

This script performs basic speech signal processing on the given audio file.

Processing steps:
- Loads the audio waveform using `librosa`
- Plots:
  - waveform
  - spectrogram (time–frequency distribution)
  - RMS energy curve
- These visualisations help understand pauses, energy fluctuations, speaking rate, and possible regions impacting ASR performance.

## 2. Instructions to Run the Code

### 2.1 Install Required Libraries

Use the following commands to install dependencies:

pip install pandas jiwer librosa matplotlib numpy


### 2.2 Run ASR Evaluation

python evaluate_asr.py

This will:
- Read both ASR TSV input files
- compute sentence-level and corpus-level WER and CER
- generate output result files:
  - `asr1_results.csv`
  - `asr2_results.csv`
- print the summary performance values in the terminal

### 2.3 Run Audio Analysis and Plot Generation

python audio_visualize.py

This will display three plots sequentially:
1. waveform
2. spectrogram
3. RMS energy

These visualisations can be saved as screenshots and inserted into the final report.

## 3. Explanation of WER and CER

### Word Error Rate (WER)

WER measures the difference between the ASR output and the reference transcript at the word level.  
It is calculated using:

WER = (Substitutions + Deletions + Insertions) / Total number of reference words

Where:
- Substitution (S): a wrong word is produced instead of the correct one
- Deletion (D): a word from the reference is missing
- Insertion (I): an extra word not spoken is produced

A lower WER indicates better ASR performance.

### Character Error Rate (CER)

CER evaluates transcription accuracy at the character level.  
It uses the same concept as WER, but compares characters rather than words.  
This metric is useful for spotting spelling errors and finer recognition issues.

Both WER and CER were computed using the `jiwer` library, which aligns the reference transcript and ASR output to count substitutions, deletions, and insertions.

## 4. Analysis of Results and Performance Comparison

After running the evaluation:

| ASR System | WER (approx.) | CER (approx.) |
|------------|---------------|---------------|
| ASR1       | 0.27          | 0.13          |
| ASR2       | 0.47          | 0.22          |

### Interpretation

- ASR1 produces fewer errors than ASR2 at both the word and character levels.
- ASR2 shows higher substitution, deletion, and insertion error counts.
- ASR1 maintains better alignment with the human reference transcript and preserves sentence structure more reliably.

### Conclusion

ASR1 performs significantly better than ASR2 based on both WER and CER metrics.  
Therefore, ASR1 is the preferred ASR system for this dataset.

## 5. Signal Processing Analysis of the Audio File

Three audio signal visualisation plots were generated to help understand acoustic characteristics and relate them to ASR performance.

## 5.1 Waveform Interpretation

The waveform shows multiple spoken segments separated by noticeable silence intervals.  
Strong high-amplitude regions indicate active speech, while nearly flat sections represent pauses or transitions between phrases.  
The distribution of speech across the recording suggests the speaker delivered information in separate units rather than continuous speech.  
These pauses likely influence ASR alignment and segmentation behaviour.

---

## 5.2 Spectrogram Interpretation (dB Scale)

The spectrogram reveals dominant speech energy concentrated below approximately 6 kHz, consistent with natural spoken voice spectra.  
Harmonic bands and formant structures appear during voiced segments, while silence regions show almost no activity.  
Variations in spectral density across segments suggest differences in articulation clarity, which can relate to ASR performance differences for certain phrases.

---

## 5.3 RMS Energy Curve Interpretation

The RMS energy plot clearly matches the waveform — high peak areas align with voiced speech, while near-zero values mark pauses.  
The rising and falling envelope pattern indicates natural rhythm and stress variation in speech delivery.  
Segments with stronger energy levels likely supported better ASR recognition, whereas lower-energy or softer regions may correspond to recognition errors.

---

### Summary of Observations Across Plots

- All three plots consistently show distinct voiced regions separated by silence.
- The spectrogram’s concentrated low-frequency structure aligns with typical conversational speech.
- Segment-level energy changes explain why some phrases would be easier for ASR systems to decode than others.
- High peak regions correlate with clearer articulation, supporting the hypothesis that ASR1 handled speech better than ASR2.

Screenshots of all three plots are included in the report PDF and saved separately in this repository.


## 6. Repository Contents

The repository includes:

- `evaluate_asr.py` – code for computing sentence-level and corpus-level WER/CER
- `audio_visualize.py` – code for generating waveform, spectrogram, and RMS plots
- `single_s1_22032_11908_asr1.tsv` – ASR system output with timestamps and reference
- `single_s1_22032_11908_asr2.tsv` – second ASR system output with timestamps and reference
- `asr1_results.csv` and `asr2_results.csv` – generated evaluation output files
- final written report in PDF format containing analysis and figures

---

## 7. Acknowledgment

Dataset and evaluation task instructions were provided by  
SPIRE Lab, Indian Institute of Science (IISc), Bengaluru.

---

## 8. Author

Vamsi Krishna





