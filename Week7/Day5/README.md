# Week 7 - Day 5: Advancing the Core Model & Sprint Review

## Overview
This notebook advances the heart disease prediction project by selecting and tuning a model suited for tabular clinical data. Gradient Boosting was evaluated through manual experiments, cross-validation, and threshold optimization, then compared with previous Sprint 1 models.

## Workflow
- Selected Gradient Boosting for tabular data
- Tested multiple manual configurations
- Applied 5-fold Stratified GridSearchCV
- Evaluated the learning curve
- Optimized the classification threshold using OOF predictions
- Performed one final evaluation on the untouched test set
- Compared Sprint 2 results with previous models

## Final Results

| Model | F1-Score |
|---|---:|
| Logistic Regression Baseline | 0.899 |
| Sprint 1 Regularized Neural Network | 0.882 |
| Sprint 2 Gradient Boosting | 0.896 |

## Conclusion
Gradient Boosting was the strongest Sprint 2 candidate and improved over the Sprint 1 neural network. However, it did not surpass the Logistic Regression baseline, with only a 0.003 difference in F1-score.

The main Sprint 2 lesson is that increasing model complexity does not necessarily produce better performance. Sprint 3 will focus on feature engineering and additional tabular models.