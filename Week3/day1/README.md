# Day 1 – Supervised Learning and Train/Test Split

## Objective

The goal of this notebook is to understand the basics of supervised learning, distinguish regression from classification, separate features and target, and perform a train/test split.

## Dataset

- Pima Indians Diabetes Database
- File: `diabetes.csv`

## Topics Covered

- Supervised learning
- Regression vs classification
- Features (X) and target (y)
- Train/test split
- The basic Scikit-learn workflow
- Why the test set must remain unseen during training

## Hands-On Lab

- Loaded the dataset using Pandas.
- Separated the input features into `X`.
- Selected `Outcome` as the target `y`.
- Split the dataset into 80% training data and 20% testing data.
- Used `random_state=42` to keep the split reproducible.
- Printed the shapes of `X_train`, `X_test`, `y_train`, and `y_test`.
- Explained why the test set should not be used during training.

## Tools Used

- Python
- Pandas
- Scikit-learn
- Jupyter Notebook

## Files

- `.ipynb`
- `diabetes.csv`

## Result

The dataset was successfully prepared for machine learning. The features and target were separated, and the data was divided into training and testing sets for fair model evaluation.