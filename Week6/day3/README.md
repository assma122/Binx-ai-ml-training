# Week 6 — Day 3: Backpropagation, Gradient Descent & Optimizers

## Overview

This notebook explores how a neural network improves its predictions through the training loop:

**Forward Pass → Loss → Backpropagation → Weight Update**

The concepts are connected to a heart disease prediction project using 918 patient records.

## Topics Covered

- Neural network training loop.
- Gradient descent and weight updates.
- Learning rate and training stability.
- Backpropagation and the chain rule.
- SGD and Adam optimizers.
- Epochs, batches, and parameter updates.
- Connection to the heart disease prediction project.

## Learning Rate Experiment

| Learning Rate | Final Loss | Observation |
|---|---:|---|
| 0.001 | 0.6467 | Training progressed slowly. |
| 0.1 | 0.1418 | Training improved steadily. |
| 5.0 | 0.6931 | Training became unstable. |

The learning rate of **0.1** performed best in the small demonstration network.

## Heart Disease Project

- Original features: **11**
- Features after preprocessing: **21**
- Training patients: **734**
- Testing patients: **184**

Proposed neural network architecture:

```text
21 inputs → 16 neurons → 8 neurons → 1 output
```

Total trainable parameters: **497**.

## Baseline Reference

| Metric | Logistic Regression |
|---|---:|
| Accuracy | 0.886 |
| Precision | 0.886 |
| Recall | 0.912 |
| F1-score | 0.899 |

Future neural network models should be evaluated against this baseline.

## Tools

- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

## References

- [TensorFlow: Automatic Differentiation](https://www.tensorflow.org/guide/autodiff)
- [TensorFlow: Adam Optimizer](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam)
- [PyTorch: Automatic Differentiation](https://docs.pytorch.org/tutorials/beginner/basics/autograd_tutorial.html)
- [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)