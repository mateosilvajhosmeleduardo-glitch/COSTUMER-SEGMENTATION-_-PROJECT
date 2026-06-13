# Figure index
All PNG files in this folder were extracted directly from the embedded outputs of `notebooks/credit_card_customer_segmentation.ipynb`. They were not redrawn or manually invented.

## Figure 1: Correlation Map Between Variables
- File: `assets/figures/01_correlation_map_between_variables.png`
- Notebook cell: `33`
- Output index: `0`
- Source excerpt: `corr_matrix = df1.select_dtypes(include=["number"]).corr() plt.figure(figsize=(14, 10)) sns.heatmap(corr_matrix, annot=True, cmap="RdBu", fmt=".2f", vmin=-1, vmax=1) plt.title("Correlation Map Between Variables", fontsize=16) plt.show()`

## Figure 2: Tenure Distribution
- File: `assets/figures/02_tenure_distribution.png`
- Notebook cell: `38`
- Output index: `0`
- Source excerpt: `plt.figure(figsize=(10, 5)) sns.countplot(x=df1["Tenure"]) plt.title("Tenure Distribution") plt.tight_layout() plt.show()`

## Figure 3: Distribution Visualization Histograms
- File: `assets/figures/03_distribution_visualization_histograms.png`
- Notebook cell: `40`
- Output index: `0`
- Source excerpt: `cols = FULL_DF.columns.tolist() n_cols = len(cols) n_rows = (n_cols + 3) // 4 fig, axs = plt.subplots(nrows=n_rows, ncols=4, figsize=(16, n_rows * 3)) axs = axs.flatten() for idx, col in enumerate(cols): sns.histplot(df1[col], color="red", ax=axs[idx], kde=False) axs[idx].set_tit`

## Figure 4: Elbow Method - KMeans
- File: `assets/figures/04_baseline_elbow_method_kmeans.png`
- Notebook cell: `43`
- Output index: `0`
- Source excerpt: `from sklearn.cluster import KMeans from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score wcss = [] k_range = range(1, 11) for k in k_range: kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) kmeans.fit(X_scaled) wcss.append(kmeans.iner`

## Figure 5: Silhouette Method - KMeans
- File: `assets/figures/05_baseline_silhouette_method_kmeans.png`
- Notebook cell: `44`
- Output index: `0`
- Source excerpt: `silhouette = [] for k in range(2, 11): kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) labels = kmeans.fit_predict(X_scaled) silhouette.append(silhouette_score(X_scaled, labels)) plt.figure(figsize=(7, 4)) plt.plot(range(2, 11), silhouette, marker='o') plt.xlabel('Numbe`

## Figure 6: Balance vs Purchases
- File: `assets/figures/06_baseline_kmeans_original_variable_scatterplots.png`
- Notebook cell: `46`
- Output index: `0`
- Source excerpt: `fig = plt.figure(figsize=(18, 6), dpi=150) plt.subplot(1, 3, 1) sns.scatterplot(data=FULL_DF, x="Balance", y="Purchases", hue="Cluster_KMeans", palette=["blue", "green", "red"]) plt.title("Balance vs Purchases", fontsize=14) # Un tamaño menor para que quepa bien plt.xticks(rotati`

## Figure 7: Elbow Method - KMeans
- File: `assets/figures/07_kmeans_validation_elbow_method.png`
- Notebook cell: `52`
- Output index: `0`
- Source excerpt: `wcss = [] k_range = range(1, 11) for k in k_range: kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) kmeans.fit(X_scaled) wcss.append(kmeans.inertia_) plt.figure(figsize=(7, 4)) plt.plot(k_range, wcss, marker="o") plt.xlabel("Number of clusters (k)") plt.ylabel("WCSS / In`

## Figure 8: Silhouette Method - KMeans
- File: `assets/figures/08_kmeans_validation_silhouette_method.png`
- Notebook cell: `53`
- Output index: `0`
- Source excerpt: `silhouette = [] for k in range(2, 11): kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) labels = kmeans.fit_predict(X_scaled) silhouette.append(silhouette_score(X_scaled, labels)) plt.figure(figsize=(7, 4)) plt.plot(range(2, 11), silhouette, marker='o') plt.xlabel('Numbe`

## Figure 9: Customer distribution by cluster - KMeans
- File: `assets/figures/09_customer_distribution_by_kmeans_cluster.png`
- Notebook cell: `55`
- Output index: `2`
- Source excerpt: `k_kmeans = 3 kmeans = KMeans(n_clusters=k_kmeans, random_state=42, n_init=10) labels_kmeans = kmeans.fit_predict(X_scaled) df_kmeans = FULL_DF.copy() df_kmeans["Cluster_KMeans"] = labels_kmeans print("Customer distribution by cluster:") display(df_kmeans["Cluster_KMeans"].value_c`

## Figure 10: Cumulative variance PCA
- File: `assets/figures/10_pca_cumulative_variance.png`
- Notebook cell: `58`
- Output index: `1`
- Source excerpt: `pca = PCA() pca.fit(X_scaled) pca_variance = pd.DataFrame({ "Component": [f"PC{i+1}" for i in range(len(pca.explained_variance_ratio_))], "Explained_Variance": pca.explained_variance_ratio_, "Cumulative_Variance": np.cumsum(pca.explained_variance_ratio_) }) display(pca_variance.r`

## Figure 11: KMeans clusters visualized with 2D PCA
- File: `assets/figures/11_kmeans_clusters_visualized_with_2d_pca.png`
- Notebook cell: `66`
- Output index: `0`
- Source excerpt: `plt.figure(figsize=(7, 5)) sns.scatterplot(data=pca_2_df, x="PC1", y="PC2", hue="Cluster_KMeans", palette="viridis", alpha=0.6) plt.title("KMeans clusters visualized with 2D PCA") plt.show()`

## Figure 12: Elbow Method - KMeans
- File: `assets/figures/12_kmeans_on_pca_elbow_method.png`
- Notebook cell: `78`
- Output index: `0`
- Source excerpt: `wcss = [] k_range = range(1, 11) for k in k_range: kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) kmeans.fit(X_pca_model) wcss.append(kmeans.inertia_) plt.figure(figsize=(7, 4)) plt.plot(k_range, wcss, marker="o") plt.xlabel("Number of clusters (k)") plt.ylabel("WCSS /`

## Figure 13: Silhouette Method - KMeans
- File: `assets/figures/13_kmeans_on_pca_silhouette_method.png`
- Notebook cell: `79`
- Output index: `0`
- Source excerpt: `silhouette = [] for k in range(2, 11): kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) labels = kmeans.fit_predict(X_pca_model) silhouette.append(silhouette_score(X_pca_model, labels)) plt.figure(figsize=(7, 4)) plt.plot(range(2, 11), silhouette, marker='o') plt.xlabel(`

## Figure 14: GMM component selection
- File: `assets/figures/14_gmm_component_selection_bic.png`
- Notebook cell: `85`
- Output index: `0`
- Source excerpt: `from sklearn.mixture import GaussianMixture bic = [] aic = [] k_range_gmm = range(1, 11) for k in k_range_gmm: gmm = GaussianMixture(n_components=k, covariance_type="full", random_state=42, n_init=5) gmm.fit(X_scaled) bic.append(gmm.bic(X_scaled)) plt.figure(figsize=(7, 4)) plt.p`

## Figure 15: GMM clusters visualized with 2D PCA
- File: `assets/figures/15_gmm_clusters_visualized_with_2d_pca.png`
- Notebook cell: `87`
- Output index: `0`
- Source excerpt: `gmm_pca_plot = pd.DataFrame( X_pca_8, columns=[f"PC{i+1}" for i in range(X_pca_8.shape[1])] ) gmm_pca_plot["Cluster_GMM"] = labels_gmm gmm_pca_plot["Prob_Max_GMM"] = probs_gmm.max(axis=1) plt.figure(figsize=(7, 5)) sns.scatterplot( data=gmm_pca_plot, x="PC1", y="PC2", hue="Cluste`

## Figure 16: Eigenvalues
- File: `assets/figures/16_factor_analysis_eigenvalues.png`
- Notebook cell: `96`
- Output index: `0`
- Source excerpt: `import numpy as np import matplotlib.pyplot as plt Sigma = np.cov(X_scaled, rowvar=False) eigvals, eigvecs = np.linalg.eigh(Sigma) idx = np.argsort(eigvals)[::-1] eigvals = eigvals[idx] plt.scatter(range(1, len(eigvals)+1), eigvals) plt.plot(range(1, len(eigvals)+1), eigvals) plt`

## Figure 17: Elbow Method
- File: `assets/figures/17_factor_clustering_elbow_method.png`
- Notebook cell: `109`
- Output index: `0`
- Source excerpt: `plt.figure(figsize=(7, 4)) plt.plot(range(2,10), wcss, marker='o') plt.xlabel("Number of clusters (k)") plt.ylabel("WCSS") plt.title("Elbow Method") plt.show() plt.figure(figsize=(7, 4)) plt.plot(range(2,10), silhouette, marker='o') plt.xlabel("Number of clusters (k)") plt.ylabel`

## Figure 18: Silhouette Analysis
- File: `assets/figures/18_factor_clustering_silhouette_analysis.png`
- Notebook cell: `109`
- Output index: `1`
- Source excerpt: `plt.figure(figsize=(7, 4)) plt.plot(range(2,10), wcss, marker='o') plt.xlabel("Number of clusters (k)") plt.ylabel("WCSS") plt.title("Elbow Method") plt.show() plt.figure(figsize=(7, 4)) plt.plot(range(2,10), silhouette, marker='o') plt.xlabel("Number of clusters (k)") plt.ylabel`

## Figure 19: KMeans on factors
- File: `assets/figures/19_kmeans_on_factors.png`
- Notebook cell: `114`
- Output index: `0`
- Source excerpt: `plt.figure(figsize=(7, 5)) sns.scatterplot(x=factor_scores_df["Factor_1"], y=factor_scores_df["Factor_2"], hue=labels_fa, palette="viridis", alpha=0.6) plt.title("KMeans on factors") plt.xlabel("Factor 1") plt.ylabel("Factor 2") plt.show()`

## Figure 20: GMM component selection
- File: `assets/figures/20_gmm_factor_component_selection_bic.png`
- Notebook cell: `121`
- Output index: `0`
- Source excerpt: `from sklearn.mixture import GaussianMixture bic = [] k_range_gmm = range(1, 11) for k in k_range_gmm: gmm = GaussianMixture(n_components=k, covariance_type="full", random_state=42, n_init=5) gmm.fit(X_scaled) bic.append(gmm.bic(X_scaled)) plt.figure(figsize=(7, 4)) plt.plot(k_ran`

## Figure 21: GMM clusters visualized with 2D factors
- File: `assets/figures/21_gmm_clusters_visualized_with_2d_factors.png`
- Notebook cell: `123`
- Output index: `0`
- Source excerpt: `gmm_pca_plot = pd.DataFrame( factor_scores_df, columns=[f"Factor_{i+1}" for i in range(factor_scores_df.shape[1])] ) gmm_pca_plot["Cluster_GMM"] = labels_gmm gmm_pca_plot["Prob_Max_GMM"] = probs_gmm.max(axis=1) plt.figure(figsize=(7, 5)) sns.scatterplot( data=gmm_pca_plot, x="Fac`
