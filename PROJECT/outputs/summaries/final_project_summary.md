# Final Project Summary

## Best Test-Set Result
Random Forest achieved the highest held-out test performance:
- Accuracy: 0.885
- Precision: 0.839
- Recall: 0.929
- F1-score: 0.881
- ROC-AUC: 0.954

## Cross-Validation
Logistic Regression had the higher mean 5-fold CV F1-score:
- Logistic Regression: 0.806
- Random Forest: 0.775

## Main EDA Findings
- The classes were fairly balanced.
- thal and ca had the strongest positive correlations with the target.
- thalach had the strongest negative correlation.
- Several useful patterns were also visible in exang, oldpeak, and cp.

## Feature Engineering
Two simple engineered features were tested. Neither improved Logistic Regression performance.

## Final Interpretation
Random Forest was stronger on the held-out test set, while Logistic Regression was more consistent across cross-validation folds. The project shows why final model evaluation should use more than one metric and more than one data split.
