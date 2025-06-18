import pandas as pd

notes = pd.read_csv("mimic-iii-clinical-database-demo-1.4/NOTEEVENTS.csv")
diagnoses = pd.read_csv("mimic-iii-clinical-database-demo-1.4/DIAGNOSES_ICD.csv")

note_hadm_ids = set(notes["hadm_id"].dropna())
diag_hadm_ids = set(diagnoses["hadm_id"].dropna())

intersection = note_hadm_ids.intersection(diag_hadm_ids)

print(f"NOTEEVENTS hadm_id count: {len(note_hadm_ids)}")
print(f"DIAGNOSES_ICD hadm_id count: {len(diag_hadm_ids)}")
print(f"Matching hadm_ids: {len(intersection)}")
