import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, classification_report
import joblib

# Load cleaned data
df = pd.read_csv("synthetic_ICD-10_Dataset.csv")

# Debug: show content stats
print(" Sample rows:")
print(df.head(3))
print(" clean_text sample:")
print(df["clean_text"].head(10))
print(" Missing clean_text rows:", df["clean_text"].isna().sum())
print(" clean_text lengths:", df["clean_text"].str.len().describe())

#  Filter out rows where clean_text is empty or null
df = df[df["clean_text"].notna() & (df["clean_text"].str.strip() != "")]

# Convert ICD codes from string list to actual list
df["icd9_code"] = df["icd9_code"].apply(eval)

# TF-IDF Vectorization
print("Vectorizing text...")
vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df["clean_text"])
print(" Cleaned text sample:")
print(df["clean_text"].head(10))

print(" Number of empty rows:", df["clean_text"].str.strip().eq("").sum())

# Multi-label binarizer for ICD codes
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(df["icd9_code"])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression
print("Training model...")
clf = OneVsRestClassifier(LogisticRegression(max_iter=500))
clf.fit(X_train, y_train)

# Predict and evaluate
print("Evaluating...")
y_pred = clf.predict(X_test)

print("F1 score (macro):", f1_score(y_test, y_pred, average="macro"))
print(classification_report(y_test, y_pred, target_names=mlb.classes_))

# Save model and vectorizer
joblib.dump(clf, "icd_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(mlb, "icd_mlb.pkl")
print(" Model, vectorizer, and label binarizer saved.")