# Cardiac Patient Monitoring System

A machine learning project that analyzes clinical patient data, predicts heart disease, and explores patient patterns using supervised and unsupervised learning.

> This project is intended for educational analysis and does not replace professional medical diagnosis.

## Dataset

- **Dataset:** Cleveland Heart Disease
- **Records:** 303 patients
- **Input features:** 13
- **Target:** `target`
- **Target classes:**
  - `0`: No Heart Disease
  - `1`: Heart Disease

The dataset contains no missing values or duplicate records.

## Project Workflow

### Milestone 1 — Data Understanding

- Loaded the dataset and documented the clinical features.
- Checked data types, missing values, duplicates, and numerical ranges.
- Reviewed categorical feature values.
- Saved a checked copy of the dataset.

### Milestone 2 — Exploratory Data Analysis

- Examined the target distribution and descriptive statistics.
- Visualized numerical features and patient-group differences.
- Analyzed correlations and categorical features.
- Identified potential outliers using the IQR method.
- Explored the relationship between age and maximum heart rate.

### Milestone 3 — Baseline Model

- Created a stratified 80/20 train-test split.
- Applied `StandardScaler`.
- Trained Logistic Regression as the baseline classifier.
- Evaluated accuracy, precision, recall, F1-score, and the confusion matrix.

### Milestone 4 — Model Comparison and Tuning

- Trained a Random Forest classifier.
- Compared the models using the same test set.
- Examined the effect of tree depth on overfitting.
- Applied 5-fold stratified cross-validation.
- Analyzed Random Forest feature importance.
- Tuned Random Forest using `GridSearchCV`.
- Compared ROC curves and ROC-AUC scores.

### Milestone 5 — Feature Engineering and Pipeline

- Created the engineered feature:

  ```python
  thalach_age_ratio = thalach / age
  ```

- Built a reusable pipeline:

  ```text
  StandardScaler → Logistic Regression
  ```

- Compared the engineered pipeline with the original baseline.

The engineered feature did not improve test performance, but the pipeline made preprocessing and model training more consistent.

### Milestone 6 — Unsupervised Learning

- Applied PCA to the scaled clinical features.
- Examined cumulative explained variance.
- Visualized patients using two principal components.
- Applied K-Means clustering with two clusters.
- Compared the discovered clusters with the actual diagnoses.

## Model Results

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.869 | 0.812 | 0.929 | 0.867 | 0.953 |
| Random Forest | 0.885 | 0.839 | 0.929 | 0.881 | 0.954 |
| **Tuned Random Forest** | **0.902** | **0.844** | **0.964** | **0.900** | **0.959** |
| Engineered Pipeline | 0.869 | 0.812 | 0.929 | 0.867 | — |

### Cross-Validation

- Logistic Regression mean F1-score: **0.806**
- Random Forest mean F1-score: **0.775**
- Tuned Random Forest best cross-validation F1-score: **0.799**

### Best Random Forest Parameters

```python
max_depth = 7
min_samples_split = 2
n_estimators = 200
```

## PCA and Clustering Results

- The first two principal components retained **35.8%** of the total variance.
- **12 of 13 components** were needed to retain **97.3%** of the variance.
- K-Means identified two patient groups:

| Cluster | No Heart Disease | Heart Disease |
|---|---:|---:|
| Cluster 0 | 151 | 38 |
| Cluster 1 | 13 | 101 |

The clusters were created without using the target and showed a clear association with the actual diagnosis.

## Final Decision

The **Tuned Random Forest** achieved the strongest test performance:

- **Accuracy:** 0.902
- **Precision:** 0.844
- **Recall:** 0.964
- **F1-score:** 0.900
- **ROC-AUC:** 0.959

Logistic Regression achieved a slightly higher average cross-validation F1-score, so the final results should be interpreted in the context of the dataset size and evaluation method.

## Limitations

- The dataset contains only 303 patient records.
- Some categorical features remain in their original numeric encoding.
- Potential outliers were retained because they may represent real patient measurements.
- The two-dimensional PCA visualization captures only part of the total variance.
- K-Means clusters are exploratory and do not represent medical diagnoses.
- The project is not a substitute for professional clinical assessment.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open the project notebook and run the cells from top to bottom.