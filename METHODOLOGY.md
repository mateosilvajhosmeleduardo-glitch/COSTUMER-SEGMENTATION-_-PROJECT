# Methodology

This project applies unsupervised learning to a public credit card customer dataset. The main objective is to identify interpretable customer segments based on financial behavior, not to predict a target variable.

## Dataset

The dataset contains **8,950 customers** and **18 variables**, including balance, purchases, cash advances, credit limit, payments, and payment behavior indicators.

## Analytical workflow

1. **Data loading and inspection**  
   The dataset is loaded from `data/Customer_Data.csv` using a portable path so the project can run from a GitHub repository.

2. **Exploratory data analysis**  
   Descriptive statistics, missing values, distributions, outliers, and correlation patterns are examined to understand customer behavior before modeling.

3. **Preprocessing**  
   The customer identifier is removed, missing numeric values are imputed, and the variables are standardized. Standardization is necessary because the variables have very different units and magnitudes.

4. **K-Means clustering**  
   K-Means is used as the main segmentation model. The project evaluates the number of clusters using inertia and silhouette score.

5. **PCA visualization**  
   Principal Component Analysis is used to project the high-dimensional customer space into two or three components for visualization. The clustering is performed on the standardized variables, while PCA is mainly used for interpretation and plotting.

6. **Gaussian Mixture Models**  
   GMM is included as an alternative probabilistic segmentation method. This makes the analysis broader than a simple K-Means-only notebook.

7. **Exploratory Factor Analysis**  
   Factor analysis is used as an additional dimensionality reduction approach to compare latent behavioral structures with PCA.

## Main segment interpretation

The K-Means solution with three clusters produced the following behavioral profiles:

| Cluster | Segment interpretation | Customers | Share |
|---:|---|---:|---:|
| 0 | Active purchase customers | 1275 | 14.25% |
| 1 | Low-activity customers | 6114 | 68.31% |
| 2 | Cash-advance oriented customers | 1561 | 17.44% |


## Model validation summary

| Metric | Value |
|---|---:|
| Silhouette score (sample=1000) | 0.2402 |
| Calinski-Harabasz index | 1605.03 |
| Davies-Bouldin index | 1.592 |
| PCA variance PC1 | 0.273 |
| PCA variance PC2 | 0.2031 |
| PCA variance PC3 | 0.0881 |
| PCA variance PC1-PC3 | 0.5642 |


## Originality of this project

The dataset is public, so other notebooks may use the same source. The originality of this project comes from the structure of the analysis, the extended interpretations, the comparison between clustering methods, the inclusion of PCA and factor analysis, and the documentation of each table and graph.
