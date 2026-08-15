# Cardiac Patient Monitoring System

A machine learning project built on the Heart Disease Cleveland dataset to explore patient patterns, compare classification models, and evaluate model performance using a complete supervised-learning workflow.

## Project Objective

The goal of this project is to analyze cardiac-related patient data and build classification models that can distinguish between the two target classes in the dataset.

The project focuses on:
- data understanding and quality checks
- exploratory data analysis
- supervised classification
- model comparison
- cross-validation
- Random Forest depth analysis
- feature importance analysis
- hyperparameter tuning
- feature engineering
- reusable Scikit-learn pipelines
- final model evaluation

> This project is for educational machine-learning analysis only and is not intended for clinical diagnosis or treatment decisions.

## Dataset

**Dataset:** Heart Disease Cleveland  
**Records:** 303  
**Input Features:** 13  
**Target:** `target`

Target values:
- `0` = No Heart Disease
- `1` = Heart Disease

The dataset was checked for missing values, duplicate rows, coded categorical values, and unusual numerical ranges before modeling.

## Project Workflow

### Milestone 1 — Understanding the Data
- Loaded and inspected the dataset
- Created a data dictionary
- Checked missing values and duplicates
- Reviewed categorical codes
- Inspected numerical ranges
- Saved a checked version of the dataset

### Milestone 2 — Exploratory Data Analysis & Statistics
- Reviewed class balance
- Calculated descriptive statistics
- Visualized numerical distributions
- Compared patient groups using boxplots
- Studied feature correlations
- Checked potential outliers using the IQR method
- Explored categorical features
- Reviewed age and maximum-heart-rate patterns
- Calculated heart-disease probability in the dataset

### Milestone 3 — Supervised Baseline
- Defined the binary classification problem
- Used an 80/20 stratified train/test split
- Trained Logistic Regression as the baseline model
- Applied StandardScaler
- Evaluated Accuracy, Precision, Recall, and F1-score
- Reviewed the confusion matrix and classification report

### Milestone 4 — Model Comparison & Evaluation
- Trained Random Forest as the comparison model
- Compared both models using the same test split
- Tested different Random Forest tree depths using a validation split
- Reviewed Random Forest feature importance
- Applied 5-fold Stratified Cross-Validation
- Compared fold-by-fold F1-scores
- Reviewed the Random Forest confusion matrix
- Applied GridSearchCV for hyperparameter tuning
- Added ROC Curve and ROC-AUC evaluation

### Milestone 5 — Feature Engineering & Pipeline

Two engineered features were tested:

- `thalach_age_ratio = thalach / age`
- `age_oldpeak_interaction = age * oldpeak`

A reusable Scikit-learn Pipeline was created using:

`StandardScaler → LogisticRegression`

The engineered features did not improve the test performance, but the Pipeline made the preprocessing and training workflow cleaner and repeatable.

## Final Results

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.869 | 0.812 | 0.929 | 0.867 | 0.953 |
| Random Forest | 0.885 | 0.839 | 0.929 | 0.881 | 0.954 |
| **Tuned Random Forest** | **0.902** | **0.844** | **0.964** | **0.900** | — |
| Pipeline V1 | 0.869 | 0.812 | 0.929 | 0.867 | — |
| Pipeline V2 | 0.869 | 0.812 | 0.929 | 0.867 | — |

### Cross-Validation

- Logistic Regression mean F1-score: **0.806**
- Random Forest mean F1-score: **0.775**
- Tuned Random Forest best CV F1-score: **0.799**

### Hyperparameter Tuning

GridSearchCV selected:

- `max_depth = 7`
- `min_samples_split = 2`
- `n_estimators = 200`

### Main Result

The Tuned Random Forest achieved the strongest held-out test performance with an F1-score of **0.900** and recall of **0.964**.

Logistic Regression remained slightly stronger in average cross-validation performance, with a mean F1-score of **0.806** compared with **0.799** for the Tuned Random Forest.

## Key Findings

- The dataset was clean, with no missing values or duplicate rows.
- Heart disease cases represented about **45.9%** of the dataset.
- `thal` and `ca` showed the strongest positive correlations with the target.
- `thalach` showed the strongest negative correlation with the target.
- Random Forest feature importance highlighted `thalach`, `cp`, and `thal` among the most influential features.
- Deeper Random Forest trees showed a larger gap between training and validation performance, suggesting overfitting.
- Hyperparameter tuning improved the Random Forest mean CV F1-score from **0.775** to **0.799**.
- The Tuned Random Forest achieved the highest test F1-score at **0.900**.
- Logistic Regression achieved the highest mean cross-validation F1-score at **0.806**.
- Both original models achieved very high ROC-AUC scores.
- The engineered features did not improve Logistic Regression performance.
- The Pipeline improved workflow consistency even when performance stayed the same.

## Project Structure

```text
Cardiac-Patient-Monitoring-System/
│
├── data/
│   ├── Heart_disease_cleveland_new.csv
│   └── heart_cleveland_checked.csv
│
├── notebooks/
│   └── cardiac_patient_monitoring.ipynb
│
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── summaries/
│
├── README.md
└── requirements.txt