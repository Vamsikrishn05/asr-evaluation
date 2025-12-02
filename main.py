
import pandas as pd
from jiwer import wer, cer


def normalize_text(s: str) -> str:
    """
    Simple normalization:
    - convert to lowercase
    - strip leading/trailing spaces
    """
    if not isinstance(s, str):
        return ""
    return s.strip().lower()


def evaluate_one_file(tsv_path: str, out_csv: str):
    # Read TSV (tab-separated values)
    # If your file has 4 columns: start, end, asr, reference,
    # this will work even if column names are different.
    df = pd.read_csv(tsv_path, sep="\t")

    # We assume:
    # column index 2 = ASR output (hypothesis)
    # column index 3 = Reference (ground truth)
    asr_col = df.columns[2]
    ref_col = df.columns[3]

    hyp_list = []
    ref_list = []
    per_row_wer = []
    per_row_cer = []

    for _, row in df.iterrows():
        hyp = normalize_text(row[asr_col])
        ref = normalize_text(row[ref_col])

        hyp_list.append(hyp)
        ref_list.append(ref)

        if ref.strip() == "":
            per_row_wer.append(None)
            per_row_cer.append(None)
        else:
            per_row_wer.append(wer(ref, hyp))
            per_row_cer.append(cer(ref, hyp))

    # add per-sentence metrics
    df["WER_sentence"] = per_row_wer
    df["CER_sentence"] = per_row_cer

    # corpus-level metrics (all text joined)
    joined_ref = " ".join(ref_list)
    joined_hyp = " ".join(hyp_list)

    if joined_ref.strip() == "":
        corpus_wer = None
        corpus_cer = None
    else:
        corpus_wer = wer(joined_ref, joined_hyp)
        corpus_cer = cer(joined_ref, joined_hyp)

    # save detailed results
    df.to_csv(out_csv, index=False)

    print(f"==== Results for {tsv_path} ====")
    print(f"  Output CSV : {out_csv}")
    print(f"  Corpus WER : {corpus_wer}")
    print(f"  Corpus CER : {corpus_cer}")
    print()


def main():
    # *** IMPORTANT ***
    # These filenames must match exactly your TSV names in this folder.
    evaluate_one_file(
        "single_s1_22032_11908_asr1.tsv",
        "asr1_results.csv"
    )
    evaluate_one_file(
        "single_s1_22032_11908_asr2.tsv",
        "asr2_results.csv"
    )


if __name__ == "__main__":
    main()

