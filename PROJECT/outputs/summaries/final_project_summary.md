# Final Results Summary

- Tuned Random Forest achieved the strongest held-out test performance:
  - Accuracy: 0.902
  - Precision: 0.844
  - Recall: 0.964
  - F1-score: 0.900
- GridSearchCV selected:
  - max_depth = 7
  - min_samples_split = 2
  - n_estimators = 200
- Mean CV F1-score:
  - Logistic Regression: 0.806
  - Random Forest: 0.775
  - Tuned Random Forest: 0.799
- Logistic Regression remained slightly stronger than the tuned Random Forest in mean cross-validation F1-score.
- The engineered Pipeline features did not improve Logistic Regression test performance.
