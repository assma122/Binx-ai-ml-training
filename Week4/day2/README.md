# Day 2 - Cross-Validation

## Overview

In Day 1, I evaluated the model using one validation split.

In Day 2, I wanted to check if that result would stay similar when the model is evaluated on different parts of the data.

I used **5-fold cross-validation** with Logistic Regression, compared it with the Day 1 score, and then used **StratifiedKFold** because stroke cases are rare in the dataset.

---

## What I Applied

- 5-Fold Cross-Validation
- `cross_val_score`
- Mean and Standard Deviation
- F1-score
- Single Split vs Cross-Validation
- StratifiedKFold
- Class Imbalance

---

## Main Results

| Method | F1-score | Std |
|---|---:|---:|
| Day 1 Single Split | 0.249 | - |
| 5-Fold Cross-Validation | 0.234 | 0.024 |
| Stratified 5-Fold CV | 0.228 | 0.012 |

The F1-scores across the five folds ranged from about **0.197 to 0.272**.

The stroke class represented only about **4.9%** of the data, so stratification was important to keep a similar class ratio in every fold.

---

## What I Learned

A single validation split can give a slightly different result depending on which samples are selected.

Cross-validation gives a better overall view of model performance, while StratifiedKFold is especially useful here because the target is imbalanced.

---

## Tools

Python • Pandas • NumPy • Matplotlib • Scikit-learn • Jupyter Notebook