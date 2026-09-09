# Week 7 — Deep Learning Architectures

This week focused on understanding how the **type of data determines the most suitable model architecture**.

The work covered image data, sequential data, text data, and finally returned to the core Heart Disease project using tabular data.

---

## Day 1 — CNN Fundamentals

- Learned how Convolutional Neural Networks process images.
- Applied 3×3 convolution filters.
- Explored:
  - Feature Maps
  - Stride
  - Padding
  - Parameter Sharing
  - Translation Invariance
- Compared Dense and Conv2D parameter counts.
- Applied filters to melanoma images.

### Key Result

- Dense Layer Parameters: **7,680,064**
- Conv2D Parameters: **896**

This showed why CNNs are much more efficient for image data.

---

## Day 2 — Building a Complete CNN

A complete CNN was built for melanoma image classification.

Topics included:

- Conv2D
- MaxPooling
- Flatten
- Dense Layers
- Sigmoid Classification
- Data Augmentation
- Transfer Learning
- MobileNetV2
- Fine-Tuning

### Model Results

| Model | Test Accuracy |
|---|---:|
| Baseline CNN | **90.15%** |
| Data Augmentation CNN | 86.85% |
| Fine-Tuned MobileNetV2 | 88.00% |

The Baseline CNN achieved the highest test accuracy and provided the best balance between performance and training cost.

---

## Day 3 — RNN & LSTM for ECG Sequences

The focus moved from spatial image data to sequential ECG signals.

Topics included:

- Sequential Data
- RNN
- Hidden State
- Vanishing Gradient
- LSTM
- Forget, Input, and Output Gates
- GRU
- Class Imbalance
- Class Weights
- Padding

### Validation Results

| Model | Validation Accuracy |
|---|---:|
| Improved RNN | 89.24% |
| Standard LSTM | 84.36% |
| Tuned LSTM | **92.50%** |

### Final Tuned LSTM Test Results

- Test Accuracy: **92.36%**
- Macro F1: **71.53%**
- Weighted F1: **92.77%**

The difference between Macro and Weighted F1 highlighted the effect of class imbalance on minority heartbeat classes.

---

## Day 4 — Attention & Transformers

This day introduced Transformer-based text processing.

Topics included:

- Attention
- Self-Attention
- Query, Key, and Value
- Scaled Dot-Product Attention
- Positional Encoding
- Transformer Architecture
- BERT
- DistilBERT
- GPT-2
- Hugging Face Transformers
- Transformer Inference
- Fine-Tuning

A phishing email classifier was built using **DistilBERT**.

### Dataset

- Original Emails: **60,000**
- Cleaned Emails: **53,611**
- Legitimate: **25,988**
- Phishing: **27,623**

### DistilBERT Test Results

- Accuracy: **96.70%**
- Precision: **98.20%**
- Recall: **95.34%**
- F1-score: **96.75%**

### Confusion Matrix

- True Negatives: **476**
- True Positives: **491**
- False Positives: **9**
- False Negatives: **24**

A simple phishing detection prototype was also created and tested on different phishing writing styles.

---

## Day 5 — Gradient Boosting for Heart Disease

The final day returned to the core **Heart Disease Prediction** project.

Since the dataset is structured tabular data, **Histogram-based Gradient Boosting** was selected as a suitable candidate.

Topics included:

- Gradient Boosting
- Histogram-based Training
- Manual Hyperparameter Tuning
- GridSearchCV
- Stratified Cross-Validation
- Learning Curves
- Out-of-Fold Predictions
- Threshold Optimization
- Data Leakage Prevention

### Manual Tuning

- Initial Validation F1: **0.835**
- Best Manual F1: **0.892**
- Best Manual Recall: **0.914**

### GridSearchCV

- 324 parameter combinations
- 5 Stratified folds
- Total fits: **1,620**
- Best Mean CV F1: **0.883**

### Threshold Optimization

- Best Threshold: **0.51**
- OOF F1: **0.885**

### Final Gradient Boosting Test Results

- Accuracy: **0.886**
- Precision: **0.909**
- Recall: **0.882**
- F1-score: **0.896**

### Final Model Comparison

| Model | F1 | Recall |
|---|---:|---:|
| Logistic Regression | **0.899** | **0.912** |
| Regularized Neural Network | 0.882 | — |
| Gradient Boosting | 0.896 | 0.882 |

Although Gradient Boosting performed strongly and outperformed the Neural Network, Logistic Regression remained the best overall core model based on F1-score and Recall.

---

## Key Takeaway

The main lesson from Week 7 is that **model selection should start from the structure of the data**.

- Images → CNN
- Sequences → RNN / LSTM
- Text → Transformers
- Tabular Data → Gradient Boosting / Traditional ML

A more complex architecture does not automatically guarantee better performance. Final model selection should be based on evaluation metrics, generalization, and the requirements of the problem.