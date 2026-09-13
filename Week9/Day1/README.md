# Week 9 — Day 1
## Sprint 4 Planning, Serialization & MLOps

This notebook starts the deployment phase of the IMDb Sentiment Analysis project.

The goal of Day 1 is to prepare the trained machine learning workflow for deployment by defining the Sprint 4 plan, saving the trained model and TF-IDF vectorizer, verifying that the saved artifacts can be reused successfully, and preparing a reproducible environment.

---

## Objectives

By the end of this notebook, we:

- Defined the Sprint 4 deployment goal and backlog.
- Recreated the IMDb sentiment classification workflow.
- Serialized the trained Logistic Regression model.
- Serialized the fitted TF-IDF vectorizer.
- Loaded the saved artifacts successfully.
- Reproduced a known sentiment prediction.
- Reviewed important MLOps and reproducibility concepts.
- Created a pinned `requirements.txt` file.

---

## Deployment Workflow

The project follows this deployment path:

**Notebook → Serialization → FastAPI → Streamlit → Public Deployment**

Day 1 focuses mainly on preparing the trained model and its required artifacts for the next stages.

---

## Model Workflow

The sentiment analysis pipeline uses:

- Text preprocessing with NLTK
- TF-IDF feature extraction
- Logistic Regression classification
- Binary sentiment labels:
  - `0` → Negative
  - `1` → Positive

The TF-IDF vectorizer uses a maximum of **5,000 features**.

---

## Text Preprocessing

The preprocessing pipeline includes:

- HTML decoding
- HTML tag removal
- Negation preservation
- Lowercasing
- Number removal
- Punctuation cleaning
- Tokenization
- Stopword removal
- POS tagging
- WordNet lemmatization

The same preprocessing logic must also be used during deployment so that incoming reviews are transformed consistently with the training data.

---

## Model Serialization

The trained model and TF-IDF vectorizer are saved using `joblib`.

Generated artifacts:

```text
model.joblib
vectorizer.joblib