# Day 3 - Bias-Variance & Diagnosing Model Fit

## Overview

This notebook explores underfitting, overfitting, and the effect of Decision Tree complexity using the Healthcare Stroke Dataset.

The models are compared using training and validation F1-scores.

## Quick Navigation

- [Underfitting and Overfitting](#31---underfitting-and-overfitting)
- [Bias-Variance Trade-off](#32---bias-variance-trade-off)
- [Diagnosing Model Fit](#33---how-to-diagnose-model-fit)
- [Reducing Overfitting](#34---reducing-overfitting)
- [Hands-On Lab](#hands-on-lab)
- [Model Comparison](#step-4---final-diagnosis)

## Hands-On Lab

The hands-on part includes:

- [Step 1 - Create an Overfit Decision Tree](#step-1---deliberately-overfit-a-model)
- [Step 2 - Create an Underfit Decision Tree](#step-2---deliberately-underfit-a-model)
- [Step 3 - Reduce Tree Complexity](#step-3---reduce-model-complexity)
- [Compare Different Tree Depths](#tree-depth-comparison)
- [Step 4 - Compare the Final Models](#step-4---final-diagnosis)

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