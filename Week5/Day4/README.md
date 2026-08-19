# Day 4 — t-SNE & Anomaly Detection

## Introduction

High-dimensional sensor data is difficult to understand using normal plots. In this notebook, I used t-SNE to create a clearer 2D view of human activity patterns. I also used Isolation Forest to find sensor records that behave differently from the majority.

## Objectives

- Apply t-SNE to high-dimensional data.
- Understand the difference between PCA and t-SNE.
- Visualize local activity patterns in two dimensions.
- Explain anomaly detection and why it is often unsupervised.
- Detect unusual records using Isolation Forest.
- Understand the effect of the contamination parameter.
- Inspect flagged records and suggest possible reasons.

## Dataset

The Human Activity Recognition dataset contains:

- 10,299 sensor records
- 561 sensor features
- 6 human activities

The training and testing files were combined because the goal was visualization and unsupervised anomaly detection rather than evaluating a prediction model.

## What I Did

- Loaded and combined the dataset
- Checked and scaled the sensor features
- Selected 3,000 records for faster t-SNE visualization
- Applied t-SNE to create a 2D activity map
- Compared the t-SNE and PCA views
- Applied Isolation Forest using 5% contamination
- Compared anomaly rates across activities
- Inspected the two most unusual records

## Main Results

- The first two PCA components retained **57.03%** of the total variance.
- t-SNE displayed clearer local activity groups than PCA.
- Stationary and walking activities appeared on mostly different sides of the t-SNE plot.
- Isolation Forest flagged **515 records**, representing **5%** of the dataset.
- `WALKING_DOWNSTAIRS` had the highest anomaly rate at **22.40%**.
- Records `3935` and `3936` showed large deviations in gyroscope-energy features.

## Conclusion

PCA was useful for showing the overall variance, while t-SNE made the local activity groups easier to see. Isolation Forest helped identify records that deserve further investigation.

The detected anomalies are not confirmed errors. They may represent unusual movements or temporary sensor noise because the dataset does not provide true anomaly labels.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook