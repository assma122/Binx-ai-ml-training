# Day 2 — DBSCAN & Hierarchical Clustering

## Introduction

In Day 2, I continued exploring unsupervised learning by comparing different clustering methods on the same customer dataset.

After using K-Means in Day 1, I focused on understanding its limitations and testing two alternative methods: DBSCAN and Hierarchical Clustering.

The main goal was to see how different algorithms can interpret the same data in different ways.

## Objectives

- Understand the main limitations of K-Means.
- Apply DBSCAN and identify clusters and noise points.
- Understand the effect of `eps` and `min_samples`.
- Apply Hierarchical Clustering using Ward linkage.
- Build and interpret a dendrogram.
- Choose a suitable cut height.
- Compare K-Means, DBSCAN, and Hierarchical Clustering.

## What I Worked On

- Tested DBSCAN using different `eps` values.
- Selected `eps = 0.3` for the final DBSCAN result.
- Detected 2 clusters and 47 noise points.
- Built a hierarchical clustering model.
- Used a dendrogram to select a cut height.
- Obtained 3 hierarchical clusters.
- Compared all three clustering methods.

## Main Results

- **K-Means:** 3 clusters
- **DBSCAN:** 2 clusters + 47 noise points
- **Hierarchical Clustering:** 3 clusters

## Conclusion

Each clustering method gave a different view of the same customer data.

K-Means provided the clearest overall segmentation, Hierarchical Clustering helped show how customer groups are related, and DBSCAN was useful for identifying isolated observations as noise.