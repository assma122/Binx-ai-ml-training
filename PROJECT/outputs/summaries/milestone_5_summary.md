# Milestone 5 — Feature Engineering & Pipeline

Two engineered features were tested:

1. `thalach_age_ratio = thalach / age`
2. `age_oldpeak_interaction = age * oldpeak`

A Scikit-learn Pipeline combined StandardScaler and LogisticRegression.

Results:
- Baseline Logistic Regression F1-score: 0.867
- Pipeline V1 F1-score: 0.867
- Pipeline V2 F1-score: 0.867

The engineered features did not improve test performance, but the Pipeline made preprocessing and model training more consistent and reusable.
