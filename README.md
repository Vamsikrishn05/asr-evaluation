# ASR Evaluation Task – SPIRE Lab IISc

This repository contains code, output files, and a written report for the ASR (Automatic Speech Recognition) evaluation task assigned by the SPIRE Lab, IISc.

---

##  Contents of Repository

### ✔ Python Scripts
- `evaluate_asr.py`  
  Computes Word Error Rate (WER) and Character Error Rate (CER) for both ASR system outputs.

- `audio_visualize.py`  
  Generates a waveform, a spectrogram, and an RMS energy plot for the audio file.

---

### ✔ Data Files
- `single_s1_22032_11908_asr1.tsv`  
- `single_s1_22032_11908_asr2.tsv`  
  Contain timestamped ASR outputs and reference transcript.

- `asr1_results.csv`  
- `asr2_results.csv`  
  Evaluation outputs, including sentence-level and corpus-level error metrics.

- *(Optional)* `single_s1_22032_11908.wav`  
  Original audio file (not uploaded if size-restricted).

---

### ✔ Final Report
- `ASR_Evaluation_Report_Vamsi.pdf`  
  Includes:
  - Dataset description  
  - Evaluation methodology  
  - WER/CER results  
  - Error analysis  
  - Audio visualization screenshots  
  - Conclusion

---

##  Summary of Results

| System | WER | CER |
|-------:|----:|----:|
| **ASR1** | ~0.27 | ~0.13 |
| **ASR2** | ~0.47 | ~0.22 |

 **Conclusion:** ASR1 performs significantly better than ASR2.

---

##  How to Run Code

### Install dependencies:

```bash
pip install pandas jiwer librosa matplotlib numpy



