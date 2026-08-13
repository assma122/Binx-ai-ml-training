# Week 4 - Model Evaluation, Tuning & Pipelines

## Overview

Week 4 focused on improving the way machine learning models are evaluated, diagnosed, tuned, and organized.

Throughout the week, I worked with classification models and learned how to evaluate performance more reliably, detect overfitting and underfitting, tune hyperparameters, create new features, and finally combine the complete workflow inside a Scikit-learn Pipeline.

The week ended with a tuned end-to-end Pipeline that included feature engineering, preprocessing, model training, cross-validation, and final evaluation.

---

## Objectives

- Evaluate classification models using appropriate metrics.
- Use cross-validation for more reliable model evaluation.
- Apply StratifiedKFold to preserve class distribution.
- Understand overfitting and underfitting.
- Analyze the bias-variance tradeoff.
- Tune model hyperparameters using GridSearchCV.
- Create and evaluate engineered features.
- Compare baseline and tuned models.
- Build leak-free machine learning workflows.
- Use Pipeline and ColumnTransformer for preprocessing and modeling.
- Evaluate the final model on a held-out test set.

---

## Topics Covered

- Train, Validation, and Test Splits
- Data Leakage
- Logistic Regression
- Random Forest
- Decision Trees
- F1-score
- Cross-Validation
- StratifiedKFold
- Bias and Variance
- Overfitting and Underfitting
- Feature Engineering
- Feature Importance
- Hyperparameter Tuning
- GridSearchCV
- StandardScaler
- OneHotEncoder
- FunctionTransformer
- ColumnTransformer
- Scikit-learn Pipeline
- Confusion Matrix
- Baseline vs Tuned Model Comparison

---

## Datasets

### Stroke Dataset

Used during the first part of the week for model evaluation and diagnosing model performance.

The workflow included:

- Data preprocessing
- Train, validation, and test splitting
- Logistic Regression
- Cross-validation
- F1-score evaluation
- Decision Tree experiments
- Overfitting and underfitting analysis

### Pima Indians Diabetes Dataset

Used during the feature engineering, tuning, and Pipeline tasks.

The raw dataset contains:

- 768 records
- 8 input features
- Target: `Outcome`

Two engineered features were also created:

- `BMI_Category`
- `Glucose_Age_Risk`

---

# Daily Work

## Day 1 - Model Evaluation & Data Leakage

I prepared the dataset for model training and focused on evaluating a classification model correctly.

I worked with separate training, validation, and testing sets and applied preprocessing only to the training data to reduce the risk of data leakage.

### Main Topics

- Train / Validation / Test split
- Data preprocessing
- StandardScaler
- Logistic Regression
- F1-score
- Data leakage prevention
- Final test evaluation

---

## Day 2 - Cross-Validation

I applied cross-validation to evaluate the model across multiple data splits instead of relying on only one validation set.

`StratifiedKFold` was used to maintain a similar class distribution in every fold.

### Main Topics

- Cross-validation
- 5-fold evaluation
- StratifiedKFold
- F1-score
- Mean cross-validation performance
- More reliable model evaluation

---

## Day 3 - Bias, Variance & Diagnosing Model Fit

I explored how model complexity affects training and validation performance using Decision Trees.

Different tree depths were tested to identify overfitting and underfitting.

### Main Topics

- Bias and variance
- Overfitting
- Underfitting
- Decision Trees
- Training F1-score
- Validation F1-score
- Model complexity
- Training-validation performance gap

---

## Day 4 - Feature Engineering & Hyperparameter Tuning

I created new features and tested whether they could provide useful information to the model.

I also tuned a Random Forest model using GridSearchCV and compared different hyperparameter combinations.

### Engineered Features

- `BMI_Category`
- `Glucose_Age_Risk`

### Main Topics

- Feature engineering
- Random Forest
- Feature importance
- Hyperparameter tuning
- GridSearchCV
- Baseline model
- Tuned model
- F1-score comparison

---

## Day 5 - Scikit-learn Pipelines & Tuned Mini-Project

I combined the complete machine learning workflow into an end-to-end Scikit-learn Pipeline.

Feature engineering was included using `FunctionTransformer`, while `ColumnTransformer` handled numerical and categorical preprocessing.

The complete Pipeline was tuned using GridSearchCV with 5-fold StratifiedKFold cross-validation.

### Pipeline Flow

`Raw Data → Feature Engineering → Preprocessing → Random Forest → Prediction`

### Main Topics

- Pipeline
- FunctionTransformer
- ColumnTransformer
- StandardScaler
- OneHotEncoder
- Random Forest
- GridSearchCV
- StratifiedKFold
- Confusion Matrix
- Held-out test evaluation

### Final Day 5 Results

- Best CV F1-score: **0.645**
- Tuned Pipeline Test F1-score: **0.642**
- Baseline Pipeline Test F1-score: **0.654**

The tuned Pipeline did not outperform the baseline model on the held-out test set, showing that hyperparameter tuning does not always guarantee better unseen-data performance.

---

## What I Learned

During Week 4, I learned that model performance should not be judged using only one train-test split.

Cross-validation gives a more reliable estimate by evaluating the model across several folds, while StratifiedKFold helps preserve the class distribution.

I also learned how model complexity can lead to overfitting or underfitting and how comparing training and validation performance can help diagnose these problems.

Feature engineering and hyperparameter tuning showed me that adding new features or changing model settings does not automatically improve performance. The results still need to be evaluated carefully.

Finally, I learned how Scikit-learn Pipelines can combine feature engineering, preprocessing, and modeling into one reproducible workflow while reducing the risk of data leakage.

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Git
- GitHub

---

## Week 4 Takeaway

Week 4 moved from simply training models to building more reliable machine learning experiments.

The main focus was not only finding a good score, but understanding how the model behaves, evaluating it correctly, avoiding data leakage, and creating a structured workflow that can be reproduced and reused.