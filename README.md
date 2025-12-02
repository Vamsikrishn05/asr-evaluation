ASR Evaluation Task – SPIRE Lab IISc

This repository contains my implementation for evaluating two Automatic Speech Recognition (ASR) outputs and analyzing their performance using Word Error Rate (WER) and Character Error Rate (CER), along with audio visualization.

 1. How the Code Works
    evaluate_asr.py

This script:

✔ Reads the provided TSV files containing:

start time

end time

ASR output

reference transcript

✔ Normalizes text (lowercasing and trimming).
✔ Computes sentence-level WER and CER.
✔ Computes corpus-level WER and CER.
✔ Saves detailed evaluation results in CSV files.
✔ Prints summary scores for comparison.

Internally, it uses the jiwer library to align the reference and hypothesis sequences and measure substitutions, deletions, and insertions to compute error rates.

 audio_visualize.py

This script:

✔ Loads the audio file
✔ Displays:

waveform

spectrogram (time-frequency plot)

RMS energy curve

These plots show:

Speech structure

Pause regions

Energy variations

Possible regions where recognition difficulty may occur

They support the interpretation of ASR behavior relative to acoustic variation.

 2. Instructions to Run
 Install requirements
pip install pandas jiwer librosa matplotlib numpy

 Run ASR evaluation
python evaluate_asr.py


This will:

✔ compute sentence-level and overall WER/CER
✔ generate output files:

asr1_results.csv

asr2_results.csv

✔ print summary accuracy for both systems

 Run audio visualization
python audio_visualize.py


This will open three plots:

waveform

spectrogram

RMS energy curve

You can just screenshot these and include them in the report, if you like.

 3. Explanation of WER & CER
 Word Error Rate (WER)

Measures the difference between ASR output and reference at the word level.

Formula:

WER = (Substitutions + Deletions + Insertions) / Total words


Lower WER = better recognition accuracy.

 Character Error Rate (CER)

Like WER, but computed at the character level.
Useful for finer text mismatch analysis.

Both metrics are calculated using the jiwer functions in Python.

 4. Analysis of Results — Which ASR Performed Better?

After running the evaluation:

System	WER	CER
ASR1	~0.27	~0.13
ASR2	~0.47	~0.22

✔ ASR1 has lower WER and CER, meaning fewer mistakes
✔ ASR2 shows more word deletions, substitutions, and insertions

 Why is ASR1 better?

Its output stays closer to the human reference

Fewer word-level and spelling-level distortions

More stable alignment with spoken content

➡ Conclusion:
ASR1 performs significantly better than ASR2 for this dataset.

 5. Files in This Repository

evaluate_asr.py

audio_visualize.py

single_s1_22032_11908_asr1.tsv

single_s1_22032_11908_asr2.tsv

asr1_results.csv

asr2_results.csv

ASR_Evaluation_Report_Vamsi.pdf

 Acknowledgment

Dataset and task description provided by
SPIRE Lab, Indian Institute of Science (IISc), Bengaluru

 Author

Vamsi Krishna
