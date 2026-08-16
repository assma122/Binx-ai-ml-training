# Week 5 — Day 1: Unsupervised Learning & K-Means Clustering

## Introduction

In this notebook, I explored the basics of unsupervised learning through K-Means clustering.

Unlike supervised learning, clustering works without predefined labels. The goal was to discover natural customer groups based on their age, annual income, and spending behavior.

---

## Learning Objectives

By the end of this notebook, I was able to:

- Understand the difference between supervised and unsupervised learning.
- Explain how K-Means clustering works.
- Prepare and scale numerical data for clustering.
- Choose a suitable number of clusters using the Elbow Method.
- Validate the selected value of `k` using the Silhouette Score.
- Visualize and interpret the final customer clusters.

---

## Dataset

The analysis was performed on a customer dataset containing:

- Age
- Annual Income
- Spending Score
- Gender
- Customer ID

For clustering, I used:

`Age`, `Annual Income`, and `Spending Score`.

Customer ID was excluded because it is only an identifier, while Gender was not used in the initial numerical clustering experiment.

---

## Hands-On Workflow

### Step 1 — Prepare and Scale the Data
Selected the numerical features, checked missing values, cleaned the data, and applied `StandardScaler`.

### Step 2 — Elbow Method
Tested values of `k` from 1 to 10 and used inertia to identify the elbow point.

### Step 3 — Silhouette Score
Compared the strongest candidates from the elbow plot.

- `k = 3` → `0.484`
- `k = 4` → `0.381`

### Step 4 — Final K-Means Model
Built the final model using:

**k = 3**

The customer clusters were then visualized using Annual Income and Spending Score.

### Step 5 — Cluster Interpretation
Compared the average age, income, and spending score of each cluster to understand the customer groups.

---

## Key Findings

K-Means discovered three different customer groups:

- **Cluster 0:** Moderate Spenders
- **Cluster 1:** High Income, Low Spending
- **Cluster 2:** Young Active Spenders

The Elbow Method and Silhouette Score both supported using three clusters.

---

## Tools & Libraries

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

## Conclusion

This notebook showed how K-Means can uncover useful patterns in unlabeled customer data.

The main takeaway was that clustering is not only about assigning customers to groups, but also about understanding what makes each group different.