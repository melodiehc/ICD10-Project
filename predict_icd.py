import joblib
import spacy

# Load trained model and tools
clf = joblib.load("icd_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
mlb = joblib.load("icd_mlb.pkl")

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Preprocess text
def clean_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Example input (replace this with any clinical note)
sample_note = """
Patient was admitted with chest pain radiating to the left arm. 
History of hypertension and high cholesterol. 
Started on aspirin and statins.
"""

print("\n🧼 Cleaning input...")
cleaned = clean_text(sample_note)
print("🔤 Cleaned:", cleaned)

# Vectorize input
X = vectorizer.transform([cleaned])

# Predict ICD codes
print("🤖 Making prediction...")
y_pred = clf.predict(X)
codes = mlb.inverse_transform(y_pred)

print("\n🩺 Predicted ICD-9 Codes:", codes)
