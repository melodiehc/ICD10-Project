import pandas as pd
import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Paths
NOTES_PATH = "mimic-iii-clinical-database-demo-1.4/NOTEEVENTS.csv"
DIAG_PATH = "mimic-iii-clinical-database-demo-1.4/DIAGNOSES_ICD.csv"

# Load data
print("Loading data...")
notes = pd.read_csv(NOTES_PATH, low_memory=False)
diagnoses = pd.read_csv(DIAG_PATH)

# Merge notes with ICD codes
print("Merging notes with ICD codes...")
merged = pd.merge(notes, diagnoses, on="hadm_id")
print("Rows after merge:", merged.shape[0])
merged = merged[["hadm_id", "text", "icd9_code"]]

# For testing: limit to 1000 rows
merged = merged.head(1000)

# Cleaning function (less aggressive)
def clean_text(text):
    if not isinstance(text, str):
        return ""
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if token.is_alpha]
    cleaned = ' '.join(tokens)
    return cleaned if cleaned else "empty"

# Apply cleaning
print("Cleaning text...")
merged["clean_text"] = merged["text"].apply(clean_text)

# Print how many empty rows were cleaned
empty_rows = merged["clean_text"].str.strip().eq("").sum()
print("Empty cleaned rows (before filtering):", empty_rows)

# Filter out true empty rows (but keep fallback 'empty' strings)
merged = merged[merged["clean_text"] != ""]

# Group ICD codes per note
print("Grouping ICD codes per hadm_id...")
grouped = merged.groupby("hadm_id").agg({
    "clean_text": "first",
    "icd9_code": lambda x: list(set(x))
}).reset_index()

# Save output
grouped.to_csv("cleaned_icd_dataset.csv", index=False)
print("✅ Saved cleaned_icd_dataset.csv with", grouped.shape[0], "rows.")
