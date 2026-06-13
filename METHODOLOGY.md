# Methodology

This document summarizes the workflow implemented in the Jupyter notebook. The purpose is to keep the repository understandable without adding results that are not supported by the notebook.

## 1. Data loading

The notebook loads the public credit card customer dataset from `data/Customer_Data.csv`. The repository includes the dataset to make the project reproducible.

## 2. Exploratory analysis

The notebook reviews the structure of the dataset, missing values, distributions, and relationships between numerical variables. The figures used in the repository are extracted from the notebook outputs.

## 3. Preprocessing

The workflow removes the customer identifier from the modeling matrix and standardizes numerical variables before applying clustering algorithms. Standardization is necessary because the original variables have different units and scales.

## 4. K-Means clustering

K-Means is used as the baseline segmentation model. The notebook evaluates different values of `k` using the elbow method and silhouette analysis, then builds the final segmentation model.

## 5. PCA visualization

Principal Component Analysis is used to project the high-dimensional customer data into a lower-dimensional space for visualization. PCA is used for interpretation and plotting, not as a replacement for the full modeling workflow unless explicitly evaluated in the notebook.

## 6. Gaussian Mixture Models

The notebook also applies Gaussian Mixture Models as a probabilistic clustering alternative. This allows the segmentation to be compared with a model that does not assign customers only by nearest centroid.

## 7. Factor Analysis

Exploratory Factor Analysis is included to represent latent behavioral dimensions and compare clustering in factor space.

## Transparency note

All graphical assets in `assets/figures/` come from the notebook embedded outputs. The repository does not include externally generated figures or synthetic charts.
