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
- Reviewed the confusion matrix

### Milestone 4 — Model Comparison & Evaluation
- Trained Random Forest as the comparison model
- Compared both models using the same test split
- Applied 5-fold Stratified Cross-Validation
- Compared fold-by-fold F1-scores
- Reviewed the Random Forest confusion matrix
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
| Pipeline V1 | 0.869 | 0.812 | 0.929 | 0.867 | — |
| Pipeline V2 | 0.869 | 0.812 | 0.929 | 0.867 | — |

### Cross-Validation

- Logistic Regression mean F1-score: **0.806**
- Random Forest mean F1-score: **0.775**

### Main Result

Random Forest achieved the strongest held-out test performance, while Logistic Regression showed stronger average performance across the cross-validation folds.

## Key Findings

- The dataset was clean, with no missing values or duplicate rows.
- Heart disease cases represented about **45.9%** of the dataset.
- `thal` and `ca` showed the strongest positive correlations with the target.
- `thalach` showed the strongest negative correlation with the target.
- Random Forest achieved the highest test F1-score at **0.881**.
- Both models achieved very high ROC-AUC scores.
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
```

## How to Run

1. Clone or download the project repository.
2. Open the project folder in Jupyter Notebook or VS Code.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Open the main notebook.
5. Restart the kernel.
6. Run all cells from top to bottom.

The notebook uses relative paths, so keep the project folders organized as shown above.

## Requirements

The project uses:
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter

Exact package requirements are listed in `requirements.txt`.

## Limitations

- The dataset contains only 303 patient records.
- Results may change with a larger dataset or a different train/test split.
- The analysis is limited to the features available in the selected dataset.
- The engineered features tested in this project did not improve final performance.
- The project is intended for educational machine-learning analysis and not for clinical use.

## Final Takeaway

This project follows a complete supervised machine-learning workflow from data understanding to final evaluation.

The strongest test-set result came from Random Forest, while Logistic Regression showed better average cross-validation performance. The project also demonstrates that good model evaluation should rely on multiple metrics, not only one score or one split.
