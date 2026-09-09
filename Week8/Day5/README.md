# Week 8 — Day 5  
## Full Evaluation, Explainability & Sprint Review

This notebook completes the final evaluation and explainability stage of the IMDb sentiment classification workflow.

The goal of Day 5 is to evaluate the model using multiple classification metrics, check class imbalance, explain model decisions using SHAP, and close Sprint 3 with a review and retrospective.

---

## Learning Objectives

By the end of this notebook, I was able to:

- Evaluate a classification model using task-appropriate metrics.
- Interpret Precision, Recall, F1-score, Accuracy, and AUC-ROC.
- Check whether class imbalance requires techniques such as SMOTE.
- Explain global model behavior using SHAP.
- Explain individual predictions using SHAP waterfall plots.
- Document model strengths and limitations.
- Complete the Sprint 3 Review and Retrospective.
- Define one concrete action for Sprint 4 deployment.

---

## Dataset

The project uses the **IMDb Movie Reviews Dataset** for binary sentiment classification.

### Target Classes

- Positive
- Negative

The dataset was checked for class imbalance and found to be approximately balanced, so SMOTE was not required.

---

## Preprocessing

The same preprocessing workflow from the previous notebook was reused to maintain consistency.

The pipeline includes:

- HTML removal
- Lowercasing
- Punctuation and number removal
- Tokenization
- Stop-word removal
- Negation preservation
- POS-aware lemmatization

Special attention was given to preserving words such as:

- `not`
- `no`
- `nor`

because negation can strongly affect sentiment.

---

## Text Representation

The cleaned reviews were converted into numerical features using:

**TF-IDF Vectorization**

```python
TfidfVectorizer(max_features=5000)