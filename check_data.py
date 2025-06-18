import pandas as pd

# Load files (adjust paths if needed)
notes = pd.read_csv("mimic-iii-clinical-database-demo-1.4/NOTEEVENTS.csv", low_memory=False)
diagnoses = pd.read_csv("mimic-iii-clinical-database-demo-1.4/DIAGNOSES_ICD.csv", low_memory=False)

print("🧾 NOTEEVENTS.csv")
print("Rows:", len(notes))
print("Columns:", notes.columns.tolist())
print()

print("🧾 DIAGNOSES_ICD.csv")
print("Rows:", len(diagnoses))
print("Columns:", diagnoses.columns.tolist())
print()

# Check overlap
note_ids = set(notes["hadm_id"].dropna())
diag_ids = set(diagnoses["hadm_id"].dropna())
overlap = note_ids.intersection(diag_ids)

print(f"🔁 Overlapping hadm_id values: {len(overlap)}")
