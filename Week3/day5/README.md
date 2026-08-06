# Day 5 - Supervised Learning Mini Project

## Introduction

This mini-project applies a complete supervised learning pipeline using the Healthcare Stroke Dataset.

The project includes data exploration, preprocessing, train/test splitting, model training, evaluation, baseline comparison, and model selection.

## Dataset

- Dataset: Healthcare Stroke Dataset
- File: `healthcare-dataset-stroke-data.csv`
- Target: `stroke`

The target contains two classes:

- 0 = No Stroke
- 1 = Stroke

Therefore, this is a binary classification problem.

## Topics Covered

- Brief Exploratory Data Analysis
- Missing Value Handling
- One-Hot Encoding
- Train/Test Split
- Feature Scaling
- Avoiding Data Leakage
- Baseline Model
- Logistic Regression
- Random Forest
- Model Evaluation
- Model Comparison

## Hands-On Lab

- Step 1: Choose a dataset and determine whether the task is regression or classification.
- Step 2: Perform brief EDA and preprocess the data.
- Step 3: Train at least two models and compare them with a baseline.
- Step 4: Select the better model and justify the choice.
- Step 5: Commit the finished notebook to GitHub.

## Models Used

- Dummy Classifier
- Logistic Regression
- Random Forest

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score

## Visualizations

- Stroke target distribution
- F1-score model comparison
- Logistic Regression confusion matrix

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Files

- `MiniProject.ipynb`
- `healthcare-dataset-stroke-data.csv`

## Outcome

Logistic Regression achieved the highest F1-score and the highest recall for stroke cases.

It was selected as the better model because detecting actual stroke patients is more important than relying on accuracy alone.