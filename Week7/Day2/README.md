# Week 7 — Day 2: CNNs & Transfer Learning

## Overview

In this notebook, I built a complete image classification pipeline for classifying melanoma skin images as **Benign** or **Malignant**.

The experiments compared three approaches:

- CNN built from scratch
- CNN with Data Augmentation
- Transfer Learning using MobileNetV2 with Fine-Tuning

## What I Worked On

- Applied MaxPooling to reduce feature-map size
- Built and trained a CNN from scratch
- Added image augmentation using flipping, rotation, and zoom
- Used MobileNetV2 pre-trained on ImageNet
- Applied freezing and fine-tuning
- Compared validation behavior, test accuracy, and training time

## Final Results

| Model | Test Accuracy |
|---|---:|
| Baseline CNN | **90.15%** |
| CNN + Augmentation | 86.85% |
| Fine-Tuned MobileNetV2 | 88.00% |

The **Baseline CNN** achieved the best test accuracy and provided the best balance between performance and computational cost.

## Dataset

Melanoma Skin Cancer Dataset — Benign vs Malignant

## Tools

Python, TensorFlow, Keras, NumPy, Pandas, and Matplotlib