# Week 7 — Day 4: Attention & Transformers

## Overview
This day focuses on Attention, Self-Attention, and Transformer architectures, with a practical application using DistilBERT for phishing email detection.

## Topics Covered
- Limitations of RNNs
- Attention and Self-Attention
- Query, Key, and Value
- Transformer Architecture
- Positional Encoding
- Pre-trained Transformers
- Hugging Face Transformers

## Hands-On Project
Built a **Phishing Email Detection** model using a pre-trained DistilBERT Transformer.

The dataset was prepared and tokenized, then DistilBERT was fine-tuned to classify emails as:

- Legitimate
- Phishing

## Results
- Accuracy: **96.10%**
- Precision: **97.41%**
- Recall: **94.95%**
- F1-score: **96.17%**

## Application
A simple prototype was created to classify new emails and return:

**Email → DistilBERT → Phishing / Legitimate + Confidence**