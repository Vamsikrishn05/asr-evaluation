ASR Evaluation Task – SPIRE Lab IISc

This repository contains my implementation for evaluating two Automatic Speech Recognition (ASR) outputs using Word Error Rate (WER) and Character Error Rate (CER), along with audio signal visualization.

1. How the Code Works
1.1 evaluate_asr.py

This script performs the ASR evaluation:

Reads TSV files containing start time, end time, ASR output, and reference transcript.

Normalizes text (lowercasing and trimming).

Computes sentence-level WER and CER using the jiwer library.

Computes overall corpus-level WER and CER.

Saves results into CSV files (asr1_results.csv, asr2_results.csv).

Prints summary WER/CER values for performance comparison.

1.2 audio_visualize.py

This script processes the audio file:

Loads the waveform using librosa.

Displays:

Waveform plot

Spectrogram (time–frequency representation)

RMS energy curve

These visualizations provide insight into the acoustic properties of speech, energy variations, pause regions, and speech articulation.

2. Instructions to Run
Install required libraries
pip install pandas jiwer librosa matplotlib numpy

Run ASR evaluation
python evaluate_asr.py


This command evaluates both ASR outputs, generates CSV result files, and prints summary accuracy metrics.

Run audio visualization
python audio_visualize.py


This command displays waveform, spectrogram, and RMS plots. Screenshots can be used in the written report.

3. Explanation of WER and CER
Word Error Rate (WER)

WER measures the difference between the ASR output and reference transcript at word level.

Formula:

WER = (Substitutions + Deletions + Insertions) / Total reference words


A lower WER indicates better transcription accuracy.

Character Error Rate (CER)

CER is similar to WER but computed at character level.
It highlights finer errors such as missing letters or incorrect spellings.

Both metrics are computed using alignment-based comparison through the jiwer library.

4. Analysis of Results

After running the evaluation:

System	WER	CER
ASR1	≈ 0.27	≈ 0.13
ASR2	≈ 0.47	≈ 0.22

Observations:

ASR1 has significantly lower WER and CER values.

ASR2 makes more substitutions, deletions, and insertions, leading to greater deviation from the reference transcript.

ASR1 maintains contextual accuracy better and aligns more closely with spoken content.

Conclusion:

ASR1 performs better than ASR2 for this dataset and is the more reliable system in this comparison.

5. Repository Contents

evaluate_asr.py

audio_visualize.py

single_s1_22032_11908_asr1.tsv

single_s1_22032_11908_asr2.tsv

asr1_results.csv

asr2_results.csv

ASR_Evaluation_Report_Vamsi.pdf

Acknowledgment

Dataset and task instructions were provided by
SPIRE Lab, Indian Institute of Science (IISc), Bengaluru.

Author

Vamsi Krishna
