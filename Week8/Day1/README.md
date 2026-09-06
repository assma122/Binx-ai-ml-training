# Week 8 — Day 1: NLP Text Preprocessing

## Overview

This notebook introduces the first NLP workflow in Week 8 using the **IMDb Dataset of 50K Movie Reviews**.

The goal is to transform raw movie reviews into cleaner, more consistent text that can later be converted into numerical features for machine-learning models.

The workflow focuses on:

- Tokenization
- Cleaning and normalization
- Stop-word removal
- POS-aware lemmatization
- Signal preservation
- Contraction refinement
- Reusable preprocessing

---

## Dataset

**Dataset:** IMDb Dataset of 50K Movie Reviews  
**Task:** Binary sentiment classification

**Columns:**
- `review`
- `sentiment`

Initial dataset size:

- **50,000 reviews**
- **25,000 positive**
- **25,000 negative**

Data-quality inspection found:

- **0 missing values**
- **418 duplicate reviews**

After removing duplicates:

- **49,582 unique reviews**
- **24,884 positive**
- **24,698 negative**

The classes remain nearly balanced, so no additional balancing step is required.

---

## NLP Preprocessing Workflow

### 1. Tokenization

A raw review is split into individual tokens so that each word or symbol can be processed separately.

For the selected review:

**Initial token count: 380**

Tokenization itself does not remove noise. It simply exposes the text as smaller units for later processing.

---

### 2. Cleaning and Normalization

The review is normalized by:

- Decoding HTML entities
- Removing HTML tags
- Converting text to lowercase
- Removing numbers
- Removing punctuation
- Removing extra whitespace

After cleaning:

**380 → 313 tokens**

This step removes structural noise while keeping the main linguistic content.

---

### 3. Stop-word Removal

Common low-information words are removed to reduce unnecessary vocabulary.

However, negation words are intentionally preserved:

- `not`
- `no`
- `nor`

This is important for sentiment analysis because negation can completely change the meaning of a sentence.

Example:

`good` ≠ `not good`

After stop-word removal:

**313 → 174 tokens**

---

### 4. POS-Aware Lemmatization

Lemmatization converts different grammatical forms into their base forms.

Examples:

- `movies → movie`
- `loved → love`
- `watching → watch`

Part-of-speech tagging is used so that words are lemmatized more accurately according to their grammatical role.

The purpose of this step is **vocabulary normalization**, not aggressive token reduction.

---

## Validation and Refinement

The processed output was inspected to verify that sentiment-critical information was preserved.

Negation remained in the text, but some contraction fragments such as:

- `n't`
- `'ll`

were still present.

The pipeline was refined so that:

- `n't` becomes `not`
- standalone apostrophe fragments are removed

Final token count:

**174 → 171 tokens**

The small reduction confirms that this stage focuses on cleanup quality rather than removing large amounts of text.

---

## Token Reduction Summary

| Stage | Token Count |
|---|---:|
| Tokenized Review | 380 |
| After Cleaning | 313 |
| After Stop-word Removal | 174 |
| Final Refined Output | 171 |

The largest reduction occurs during **cleaning** and **stop-word removal**.

---

## Reusable Preprocessing Pipeline

A reusable function was created to apply the complete preprocessing workflow consistently to new reviews.

The function includes:

1. HTML cleaning
2. Lowercasing
3. Number and punctuation removal
4. Tokenization
5. Task-aware stop-word removal
6. POS tagging
7. Lemmatization
8. Contraction refinement
9. Reconstruction of processed text

The reusable function successfully reproduced the same output as the manually demonstrated workflow.

---

## Vocabulary Exploration

To inspect the remaining vocabulary after preprocessing, a representative sample of **500 reviews** was processed.

The sample contained approximately:

**64,943 processed words**

Frequently occurring words included:

- `film`
- `movie`
- `character`
- `story`
- `watch`
- `scene`
- `love`
- `good`

These words show that meaningful movie-related vocabulary remains after preprocessing.

However, frequency alone does **not** indicate predictive importance.

Feature weighting and representation will be handled in the next NLP stage.

---

## Key Decisions

The preprocessing strategy is task-aware rather than purely aggressive.

Important choices include:

- Lowercasing to reduce unnecessary variation
- Removing HTML, punctuation, and formatting noise
- Preserving negation because it affects sentiment
- Using POS-aware lemmatization for better normalization
- Refining contraction artifacts after validation
- Removing numbers in this demonstration, while recognizing that numerical ratings may carry sentiment information in some production settings

---

## Tools Used

- Python
- Pandas
- NLTK
- Matplotlib
- WordCloud
- Jupyter Notebook / VS Code

---

## Conclusion

Day 1 transformed raw IMDb reviews into cleaner and more consistent text through tokenization, cleaning, stop-word removal, and POS-aware lemmatization.

Validation helped preserve sentiment-critical negation and identify remaining contraction artifacts.

The final reusable preprocessing pipeline now provides consistent, model-ready text for the next NLP stage:

**TF-IDF and Embeddings**