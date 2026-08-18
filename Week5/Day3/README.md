# Day 3 — Dimensionality Reduction with PCA

This notebook applies Principal Component Analysis (PCA) to the Human Activity Recognition dataset to reduce its 561 smartphone sensor features while preserving most of their variance.

## Dataset

The dataset contains:

* 10,299 observations
* 561 numerical sensor features
* 6 human activity classes
* Training and testing files combined for PCA exploration

Dataset: [Human Activity Recognition with Smartphones](https://www.kaggle.com/datasets/uciml/human-activity-recognition-with-smartphones)

## Workflow

1. Loaded and combined the dataset files.
2. Separated the sensor features from `subject` and `Activity`.
3. Checked for missing values.
4. Scaled the features using `StandardScaler`.
5. Applied PCA and analyzed explained variance.
6. Selected the number of components needed to retain 95% variance.
7. Created a 2D PCA visualization.
8. Examined the strongest feature contributions to PC1.

## Key Results

| Result                    |  Value |
| ------------------------- | -----: |
| Original features         |    561 |
| Components selected       |    104 |
| Variance retained         | 95.05% |
| Variance explained by PC1 | 50.74% |
| Variance explained by PC2 |  6.24% |
| Variance retained in 2D   | 56.98% |

## Main Finding

PCA reduced the dataset from 561 features to 104 principal components while preserving 95.05% of its variance.

The 2D projection also showed a general separation between static activities and moving activities, although similar activities still overlapped.

## Tools

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

## Conclusion

PCA successfully reduced the complexity of the dataset while preserving most of its variance. The main trade-off is that the new principal components are harder to interpret than the original sensor features.
