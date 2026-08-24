# Week 6 — Day 1: Sprint Planning & Neural Network Architecture

This notebook explores the foundations of neural networks through a heart disease classification project.

## Sprint 1 Goal

Prepare the patient dataset, understand its clinical features, and establish a baseline model for comparison with future neural networks.

## Dataset

- Dataset: Heart Failure Prediction Dataset.
- Patient records: 918.
- Original input features: 11.
- Processed features after encoding: 21.
- Target: `HeartDisease`.
- Problem type: Binary classification.

Although the dataset title includes "Heart Failure," the target indicates whether heart disease is present or absent.

## Hands-On Steps

1. Define the sprint goal and initial backlog.
2. Select the dataset and perform a brief exploratory analysis.
3. Prepare the features and train a Logistic Regression baseline.
4. Commit the notebook to a feature branch and open a draft pull request.
5. Record the baseline results that future models will be compared against.

## Data Quality Findings

The dataset contained no recorded missing values or duplicate rows.

However, further inspection identified:

- 172 cholesterol measurements recorded as zero.
- 1 resting blood pressure measurement recorded as zero.

These clinically unrealistic values were treated as missing and replaced through median imputation inside the preprocessing pipeline.

## Preprocessing Workflow

- Numerical features: median imputation and standard scaling.
- Categorical features: one-hot encoding.
- Data split: 734 training records and 184 testing records.
- Stratified splitting preserved the class distribution.
- Preprocessing was fitted using training data only.

## Baseline Results

| Metric | Score |
|--------|-------|
| Accuracy | 0.886 |
| Precision | 0.886 |
| Recall | 0.912 |
| F1-score | 0.899 |

The baseline correctly identified 93 patients with heart disease but missed 9 actual cases.

## Neural Network Foundations

The notebook explains:

- Inputs, weights, and bias.
- Weighted sums and the sigmoid activation function.
- Input, hidden, and output layers.
- The relationship between Logistic Regression and a single neuron.
- Why deeper networks can learn more complex relationships.
- Why a neural network is not guaranteed to outperform classical models on a small tabular dataset.

## Proposed Architecture

**21 inputs → 16 neurons → 8 neurons → 1 output**

The network contains two hidden layers and produces one prediction for the binary classification task.

## Baseline to Beat

- F1-score: 0.899.
- Recall: 0.912.

Future neural network models should be compared against these results using the same evaluation setup.

## References

- [Heart Failure Prediction Dataset — Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
- [Neural Networks: Nodes and Hidden Layers — Google](https://developers.google.com/machine-learning/crash-course/neural-networks/nodes-hidden-layers)
- [Pipelines and ColumnTransformer — Scikit-learn](https://scikit-learn.org/stable/modules/compose.html)
- [Deep Feedforward Networks — Deep Learning Book](https://www.deeplearningbook.org/contents/mlp.html)