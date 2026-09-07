# Week 8 — Day 2: Text Representation with TF-IDF & Word Embeddings

## Overview

Day 2 focuses on transforming cleaned text into numerical representations that machine-learning models can understand.

Using the IMDb movie review dataset prepared in Day 1, this notebook explores two major NLP representation families:

- Frequency-based representations using TF-IDF
- Semantic representations using pre-trained word embeddings

The practical work also evaluates TF-IDF as a sentiment-classification baseline and explores the semantic structure captured by GloVe embeddings.

---

## Learning Objectives

By the end of this notebook, the following objectives are covered:

- Convert cleaned text into numerical vectors using TF-IDF.
- Understand Bag-of-Words and TF-IDF weighting.
- Explain how word embeddings represent semantic meaning.
- Explore semantic relationships using pre-trained GloVe embeddings.
- Compare TF-IDF, word embeddings, and contextual embeddings.
- Select an appropriate text representation for a given NLP task.

---

## Dataset

**Dataset:** IMDb Dataset of 50K Movie Reviews

**Task:** Binary Sentiment Classification

**Target Classes:**

- Positive
- Negative

The same dataset and preprocessing decisions from Day 1 were reused to maintain consistency across the NLP workflow.

After duplicate removal, the dataset contains:

**49,582 unique reviews**

---

## Day 1 Preprocessing Reuse

The Day 1 preprocessing pipeline was reused before text representation.

The pipeline includes:

- HTML decoding
- HTML tag removal
- Lowercasing
- Number removal
- Punctuation removal
- Tokenization
- Task-aware stop-word removal
- Negation preservation
- POS-aware lemmatization
- Contraction refinement

Negation words such as:

- `not`
- `no`
- `nor`

were preserved because they can significantly change sentiment meaning.

Processed reviews were cached in:

`processed_imdb_reviews.csv`

This avoids repeating the full preprocessing stage every time the notebook is executed.

---

## 1. From Text to Numbers

Machine-learning models cannot directly process natural-language text.

After preprocessing, text must be converted into numerical vectors.

Two main representation families were explored:

### Frequency-Based Representation

Methods such as Bag-of-Words and TF-IDF represent documents according to the words they contain and how important those words are.

### Semantic Representation

Word embeddings represent words as dense vectors in which words used in similar contexts occupy nearby positions in vector space.

---

## 2. Bag-of-Words and TF-IDF

### Bag-of-Words

Bag-of-Words represents a document according to word occurrence or frequency while ignoring word order.

### TF-IDF

TF-IDF stands for:

**Term Frequency — Inverse Document Frequency**

It combines two ideas:

- **Term Frequency (TF):** how frequently a term appears in a document.
- **Inverse Document Frequency (IDF):** how rare or distinctive that term is across the complete document collection.

Common terms receive lower importance, while more distinctive terms can receive higher weights.

---

## TF-IDF Data Split

The processed dataset was split before fitting the vectorizer to prevent data leakage.

### Training Set

**39,665 reviews**

- Positive: 19,907
- Negative: 19,758

### Testing Set

**9,917 reviews**

- Positive: 4,977
- Negative: 4,940

An 80/20 stratified split was used to preserve class balance.

---

## TF-IDF Representation

The TF-IDF vectorizer was configured with:

```python
TfidfVectorizer(max_features=5000)