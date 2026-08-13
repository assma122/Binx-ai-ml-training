# Week 4 - Day 5: Scikit-learn Pipelines & Tuned Mini-Project

## Overview

In Day 5, I built a complete machine learning workflow using Scikit-learn Pipelines.

The goal was to combine feature engineering, preprocessing, model training, hyperparameter tuning, cross-validation, and final evaluation in one structured workflow while reducing the risk of data leakage.

---

## Objectives

- Build a Pipeline that combines preprocessing and modeling.
- Use ColumnTransformer for numerical and categorical features.
- Add the engineered features from Day 4 into the workflow.
- Tune the full Pipeline using GridSearchCV.
- Use 5-fold cross-validation.
- Evaluate the final tuned model on a held-out test set.
- Compare the tuned model with a baseline model.

---

## Topics Covered

- Scikit-learn Pipeline
- Data leakage prevention
- ColumnTransformer
- StandardScaler
- OneHotEncoder
- FunctionTransformer
- Random Forest
- GridSearchCV
- StratifiedKFold
- F1-score
- Confusion Matrix
- Baseline vs Tuned Model Comparison

---

## Dataset

The Pima Indians Diabetes Dataset was used.

The dataset contains:

- 768 records
- 8 original input features
- 1 target column: `Outcome`

The target indicates whether a patient has diabetes.

---

## Feature Engineering

The engineered features from Day 4 were reused:

- `BMI_Category`
- `Glucose_Age_Risk`

These features were added inside the Pipeline using `FunctionTransformer`.

---

## Preprocessing

A `ColumnTransformer` was used to apply different preprocessing steps:

- Numerical features → `StandardScaler`
- Categorical features → `OneHotEncoder`

The complete workflow became:

`Raw Data → Feature Engineering → Preprocessing → Random Forest`

---

## Hyperparameter Tuning

GridSearchCV was used with 5-fold StratifiedKFold cross-validation.

The search tested 12 hyperparameter combinations, resulting in 60 Pipeline fits.

Best parameters:

```python
{
    "model__max_depth": 10,
    "model__min_samples_split": 2,
    "model__n_estimators": 100
}