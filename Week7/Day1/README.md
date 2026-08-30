# Week 7 — Day 1: CNN Fundamentals & Sprint 2 Planning

## Overview

Day 1 starts Sprint 2 by exploring the fundamentals of Convolutional Neural Networks (CNNs) and understanding why they are more suitable than dense networks for image data.

## What I Worked On

- Planned the Sprint 2 goal and backlog.
- Explored why Dense Networks struggle with image data.
- Learned convolution, filters, and feature maps.
- Experimented with stride and padding using interactive widgets.
- Applied a hand-defined edge filter to a real image.
- Compared Dense and Conv2D parameter counts.
- Explored parameter sharing and feature hierarchy.
- Selected the appropriate architecture based on the data type.

## Key Experiment

A **3 × 3 edge-detection filter** was applied to a real image to visualize how convolution transforms pixel values into a **feature map** that highlights visual boundaries.

The notebook also includes interactive experiments for:
- Different convolution filters
- Stride and padding
- A short CNN knowledge check

> Interactive widgets are available when the notebook is run in Jupyter or VS Code. GitHub displays notebook outputs statically.

## Project Decision

The main project continues with a **Dense Neural Network** because the project uses structured tabular data. CNN experiments are used separately to understand image-based deep learning.

## Files

- `Week7_Day1.ipynb` — Complete Day 1 notebook