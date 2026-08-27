# Week 6 - Day 5: Tuning, Evaluation & Sprint Review

## Overview

This notebook completes Sprint 1 by tuning the neural network systematically, using callbacks, evaluating the best saved model, and summarizing the sprint results.

## Work Completed

- Tuned one hyperparameter at a time:
  - Learning rate
  - Network size
  - Dropout rate
  - Batch size
- Used validation loss to compare experiments.
- Applied EarlyStopping and ModelCheckpoint.
- Evaluated the best model on the untouched test set.
- Compared the final metrics and analyzed the confusion matrix.
- Completed the Sprint Review and Retrospective.

## Selected Configuration

| Hyperparameter | Selected Value |
|---|---:|
| Learning Rate | 0.01 |
| Hidden Layers | 32 → 16 |
| Dropout Rate | 0.10 |
| Batch Size | 32 |
| Best Epoch | 8 |

## Final Tuned Model Results

| Metric | Score |
|---|---:|
| Accuracy | 0.859 |
| Precision | 0.896 |
| Recall | 0.843 |
| F1-score | 0.869 |
| ROC-AUC | 0.924 |

## Conclusion

Systematic tuning reduced validation loss, but it did not improve final test F1-score. The experiment showed that lower validation loss does not always guarantee stronger test performance.