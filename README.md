

# ICD10-Project
 ICD-10 Code Auto-Suggester
A Natural Language Processing (NLP) project that predicts ICD-10 codes from unstructured clinical text. Built to support medical professionals by automatically suggesting diagnosis codes from patient notes, streamlining documentation and improving workflow efficiency.


 ## Project Overview
The ICD-10 Auto-Suggester uses machine learning and NLP techniques to extract relevant information from clinical notes and match it to appropriate ICD-10 codes. This tool can be integrated into Electronic Health Record (EHR) systems to assist in faster and more accurate medical coding.

## How it Works
Input : A clinical note written by a healthcare provider

Preprocessing: Cleans the text using natural language processing, converts the text into numerical features using TF-IDF vectorization (TF-IDF: Term Frequency-Inverse Document Frequency is a statistical method used in natural language processing and information retrieval to evaluate the importance of a word in a document)

Model: Train a multi label classifier to map clean text
Output: A list of predicted ICD-10 codes relevant to the clinical note

 ## Key Features
Text preprocessing of clinical notes

Tokenization, lemmatization, and stopword removal

Multi-label classification using ICD-10 codes

Model training with traditional ML and deep learning methods

Evaluation using precision, recall, and F1-score

Web app interface for real-time predictions (in development)

 ## Tools & Technologies
Python

Pandas / NumPy

Scikit-learn / TensorFlow / Keras

NLTK / spaCy

Flask or Streamlit (for frontend demo)

MIMIC-III Dataset (for clinical text and diagnosis codes)


## How to Run
Clone the repository

Create an API Key

Install requirements: pip install -r requirements.txt

Prepare your data (or use a sample provided)

Run training: python model_train.py

Predict with test data or through the web interface

## What I Learned
Applied real-world NLP to healthcare data

Explored multi-label classification techniques

Improved understanding of clinical documentation and ICD-10 structure

Learned to manage and clean large medical datasets

Practiced collaborative version control using Git and GitHub

## Ethical Considerations
Protected Health Information (PHI) was removed or anonymized

This tool is for educational and prototyping purposes only, not intended for clinical deployment without validation and oversight

Future work includes model bias reduction and interpretability features

>>>>>>> f082fb83b211fcc33a6e55e7f180a501e4f962e1
