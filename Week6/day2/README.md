# Week 6 — Day 2: Activations, Forward Propagation & Loss

## Overview

This notebook explores how a neural network transforms patient features into a prediction and measures prediction error.

The examples are connected to a binary heart-disease classification project.

## Topics Covered

- Why neural networks need nonlinear activation functions.
- How ReLU, Sigmoid, Tanh, and Softmax differ.
- How forward propagation produces a prediction.
- How Binary Cross-Entropy measures prediction error.
- How activation and loss choices depend on the problem type.

## Activation Functions

| Function | Output Range | Typical Use |
|---|---|---|
| ReLU | 0 to positive infinity | Hidden layers |
| Sigmoid | 0 to 1 | Binary classification output |
| Tanh | -1 to 1 | Hidden layers |
| Softmax | Probabilities that sum to 1 | Multiclass classification output |

## Project Architecture

```text
21 processed inputs → Hidden layers with ReLU → 1 output with Sigmoid
```

The project uses:

- **Hidden activation:** ReLU.
- **Output activation:** Sigmoid.
- **Loss function:** Binary Cross-Entropy.
- **Task:** Binary heart-disease classification.

## Forward Pass Example

A small example network was used to demonstrate the calculation:

```text
2 inputs → 2 hidden neurons → 1 output neuron
```

Results:

```text
Hidden weighted sums: [0.78, -0.55]
After ReLU: [0.78, 0.00]
Output weighted sum: 0.502
Predicted probability: 0.623
Binary Cross-Entropy loss: 0.473
```

These values come from an illustrative example, not a trained patient model.

## Baseline Reference

The Logistic Regression baseline from Day 1 achieved:

| Metric | Score |
|---|---:|
| Accuracy | 0.886 |
| Precision | 0.886 |
| Recall | 0.912 |
| F1-score | 0.899 |

Later neural network models should be evaluated against this baseline.

## Tools

- Python
- NumPy
- Matplotlib
- Jupyter Notebook