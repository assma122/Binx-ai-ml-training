# Week 4 — Day 4: Feature Engineering & Hyperparameter Tuning


---

## Overview

This notebook focuses on improving and analyzing a Random Forest model through two main ideas:

- Feature Engineering
- Hyperparameter Tuning

The work continues from the Random Forest model used in Week 3 and applies the same dataset so the comparison remains consistent.

The main goal is not only to search for better model settings, but also to understand whether the engineered features add useful information and which hyperparameters have the strongest effect on model performance.

---

## Learning Goals

By the end of this notebook, I was able to:

- Create new features from existing dataset columns
- Apply binning and encoding to engineered features
- Distinguish model parameters from hyperparameters
- Define a hyperparameter search grid
- Use `GridSearchCV` with 5-fold cross-validation
- Compare a tuned model with an untuned baseline
- Analyze engineered feature importance
- Study which hyperparameter had the strongest effect on the F1-score

---

## Dataset Summary

| Item | Details |
|---|---|
| **Dataset** | Pima Indians Diabetes Dataset |
| **File** | `diabetes.csv` |
| **Rows** | 768 |
| **Original Columns** | 9 |
| **Target** | `Outcome` |
| **Task Type** | Binary Classification |
| **Main Model** | `RandomForestClassifier` |
| **Main Metric** | F1-score |
| **Validation Method** | 5-Fold Cross-Validation |

The target variable contains two classes:

- `0` → No Diabetes
- `1` → Diabetes

---

## Workflow

The notebook follows this sequence:

`Load Data`  
→ `Explore Dataset`  
→ `Create New Features`  
→ `Train/Test Split`  
→ `Encode Categorical Feature`  
→ `Evaluate Baseline Random Forest`  
→ `Define Hyperparameter Grid`  
→ `Run GridSearchCV`  
→ `Compare Results`  
→ `Analyze Feature & Hyperparameter Effects`

---

## Feature Engineering

Two new features were created from the original patient information.

### 1. BMI Category

The numerical `BMI` feature was grouped into four categories:

- Underweight
- Normal
- Overweight
- Obese

This makes it possible to represent BMI as broader groups instead of using only the raw numerical value.

### 2. Glucose-Age Risk

A new numerical feature was created by combining glucose level and age:

```python
df["Glucose_Age_Risk"] = df["Glucose"] * df["Age"]