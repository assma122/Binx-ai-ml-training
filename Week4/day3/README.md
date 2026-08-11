# Day 3 - Bias-Variance & Diagnosing Model Fit

## Overview

This notebook explores underfitting, overfitting, and the effect of Decision Tree complexity using the Healthcare Stroke Dataset.

The models are compared using training and validation F1-scores.

## Quick Navigation

- [Hands-On Lab](#hands-on-lab)
- [Main Results](#main-results)
- [Key Takeaway](#key-takeaway)
- [Tools](#tools)

➡️ [Open the Full Day 3 Notebook](Biase_variance.ipynb)

## Hands-On Lab

The hands-on part includes:

- Creating an overfit Decision Tree
- Creating an underfit Decision Tree
- Reducing tree complexity
- Testing different tree depths
- Comparing training and validation F1-scores

## Main Results

| Model    | Train F1 | Validation F1 |
| -------- | -------: | ------------: |
| Underfit |    0.000 |         0.000 |
| Overfit  |    1.000 |         0.179 |
| Depth 10 |    0.613 |         0.118 |

## Key Takeaway

A small train-validation gap does not always mean a good model.

Both the gap and the validation performance should be checked.

## Tools

Python · Pandas · Matplotlib · Scikit-learn · Jupyter Notebook