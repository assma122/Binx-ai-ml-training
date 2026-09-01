# Week 7 — Day 3: RNNs & LSTMs for Sequential Data

## Overview

This day focused on sequential data and how recurrent neural networks learn temporal patterns.

The main concepts covered were:
- Sequential data and why order matters
- Recurrent Neural Networks (RNNs) and hidden states
- The vanishing gradient problem
- LSTMs and GRUs
- Embeddings for sequential data

## Hands-On: ECG Heartbeat Classification

The ECG Heartbeat Categorization Dataset was used to classify heartbeat signals into five classes.

Each heartbeat contains **187 ordered ECG measurements**, making it suitable for sequence modeling with RNNs and LSTMs.

## Model Experiments

Several models were tested and improved gradually:

- Plain RNN
- Improved RNN with adjusted training settings
- RNN with softer class weights
- Standard LSTM
- Tuned LSTM

The Tuned LSTM used stacked LSTM layers, Dropout, Early Stopping, and adaptive learning-rate reduction.

## Results

| Model | Validation Accuracy |
|---|---:|
| Improved RNN | 89.24% |
| Standard LSTM | 84.36% |
| **Tuned LSTM** | **92.50%** |

### Final Test Performance

- **Test Accuracy:** 92.36%
- **Macro F1-score:** 71.53%
- **Weighted F1-score:** 92.77%

The Tuned LSTM achieved the strongest overall performance and generalized well to the unseen test set.

Class imbalance remained an important challenge, particularly for the minority heartbeat classes.

## Tools

Python · TensorFlow/Keras · Pandas · NumPy · Matplotlib · Scikit-learn