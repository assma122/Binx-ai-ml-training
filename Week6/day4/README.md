# Week 6 — Day 4: Building & Training a Neural Network in Keras

## Overview

This notebook applies the full Keras workflow to the heart-disease prediction project:

`build → compile → fit → diagnose → regularize → evaluate`

The goal is to train a neural network, inspect its learning history, reduce overfitting, and compare its performance with the Day 1 Logistic Regression baseline.

> This project is an educational machine-learning experiment and is not intended for medical diagnosis.

## Dataset

- **Dataset:** Heart Failure Prediction Dataset
- **Records:** 918
- **Original input features:** 11
- **Processed input features:** 21
- **Target:** `HeartDisease`
- **Task:** Binary classification

Numerical features were median-imputed and standardized. Categorical features were transformed using One-Hot Encoding.

## Neural Network Architecture

```text
21 inputs → 16 ReLU neurons → 8 ReLU neurons → 1 Sigmoid output
```

The basic network contains **497 trainable parameters**.

## Training Configuration

| Setting | Value |
|---|---|
| Optimizer | Adam |
| Learning rate | 0.001 |
| Loss function | Binary Cross-Entropy |
| Epochs | 50 |
| Batch size | 32 |
| Output activation | Sigmoid |

## Experiments

### Basic Neural Network

The first network learned useful patterns but showed moderate overfitting: training performance continued improving while validation performance stabilized.

### Regularized Neural Network

The second network added:

- Batch Normalization
- Dropout with a rate of `0.30`

Regularization improved accuracy and precision, but reduced recall and increased the number of false negatives.

## Final Results

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression Baseline | **0.886** | 0.886 | **0.912** | **0.899** |
| Basic Neural Network | 0.859 | 0.865 | 0.882 | 0.874 |
| Regularized Neural Network | 0.875 | **0.925** | 0.843 | 0.882 |

## Main Finding

The Regularized Neural Network produced fewer false positives, but it missed more true heart-disease cases. Logistic Regression remained the strongest overall model because it achieved the highest F1-score and recall.

This experiment demonstrates that a neural network is not automatically better than a classical model. For this relatively small, structured tabular dataset, Logistic Regression generalized more effectively.

## Hands-On Lab Completed

- Built a Keras Sequential network.
- Compiled and trained it for 50 epochs.
- Plotted training and validation loss and accuracy.
- Diagnosed moderate overfitting.
- Added Batch Normalization and Dropout.
- Evaluated both networks on the held-out test set.
- Compared the results with the Day 1 baseline.

## Files

```text
day4/
├── Week6_Day4.ipynb
└── README.md
```

