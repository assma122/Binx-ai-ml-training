# Day 1 - Train / Validation / Test Split

## Overview

In this notebook, I learned how to create a proper three-way data split for supervised machine learning.

Instead of using only training and testing sets, I divided the dataset into training, validation, and testing sets. This allows the model to be tuned using the validation set while keeping the test set untouched until the final evaluation.

---

## Learning Objectives

- Understand why a validation set is needed.
- Create a correct 60/20/20 data split.
- Train a machine learning model.
- Tune one hyperparameter using the validation set.
- Evaluate the final model on the test set only once.

---

## Topics Covered

- Train / Validation / Test Split
- Three-Way Data Split
- Model Training
- Hyperparameter Tuning
- Logistic Regression
- Validation Set Evaluation
- Final Test Evaluation
- Data Leakage

---

## Hands-On Lab

### Step 1
Created a 60/20/20 Train / Validation / Test split using `train_test_split()`.

### Step 2
Trained a Logistic Regression model and tuned the `C` hyperparameter using the validation set only.

### Step 3
Selected the best model and evaluated it on the test set exactly once.

### Step 4
Explained why tuning the model using the test set leads to misleading performance estimates.

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## Outcome

By the end of this lab, I understood how to correctly separate training, validation, and testing data, tune a model without introducing data leakage, and perform a fair final evaluation on unseen data.