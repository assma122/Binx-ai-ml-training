# Day 2 - Cross-Validation

## Overview

In this notebook, I learned how Cross-Validation can give a better idea about model performance compared with using only one validation split.

I used 5-fold cross-validation with Logistic Regression and compared the result with the single validation score from Day 1.

---

## Topics Covered

- K-Fold Cross-Validation
- 5-Fold Cross-Validation
- `cross_val_score`
- Mean F1-score
- Standard Deviation
- Single Split vs Cross-Validation
- Stratified K-Fold
- Class Imbalance

---

## Hands-On Lab

### Step 1
Evaluated a Logistic Regression model using 5-fold cross-validation.

### Step 2
Calculated the mean and standard deviation of the F1-scores across the five folds.

### Step 3
Compared the cross-validation result with the single validation score from Day 1.

### Step 4
Used StratifiedKFold to keep a similar class distribution in each fold because the stroke dataset is imbalanced.

---

## Results

- Cross-validation was evaluated using F1-score.
- The results changed slightly across the five folds.
- The single validation score from Day 1 was slightly higher than the cross-validation average.
- StratifiedKFold helped keep the class distribution more balanced across folds.

---

## Final Stratified Cross-Validation Result

- Mean F1-score: `0.228`
- Standard Deviation: `0.012`

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## Learning Outcome

By the end of this notebook, I understood why using more than one validation split can give a better view of model performance.

I also learned how the mean and standard deviation are used to understand the average performance and stability of the model across different folds.