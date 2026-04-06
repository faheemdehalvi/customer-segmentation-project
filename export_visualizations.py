#!/usr/bin/env python3
"""
Export visualizations from notebooks as PNG files for README
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

# Create reports/figures directory
os.makedirs('reports/figures', exist_ok=True)

# Load data
print("Loading data...")
data = pd.read_csv('data/processed/rfm_scaled.csv')

# Add clusters
numeric_data = data[['Recency', 'Frequency', 'Monetary']]
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
clusters = kmeans.fit_predict(numeric_data)

# 1. Elbow Curve
print("Generating Elbow Curve...")
inertia = []
K = range(1, 11)
for k in K:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(numeric_data)
    inertia.append(km.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(K, inertia, marker='o', linewidth=2, markersize=8)
plt.title('Elbow Method for Optimal k', fontsize=14, fontweight='bold')
plt.xlabel('Number of clusters (k)', fontsize=12)
plt.ylabel('Inertia', fontsize=12)
plt.xticks(K)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reports/figures/elbow_curve.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: reports/figures/elbow_curve.png")

# 2. PCA Clusters
print("Generating PCA Clusters visualization...")
pca = PCA(n_components=2)
pca_result = pca.fit_transform(numeric_data)
pca_df = pd.DataFrame(data=pca_result, columns=['PCA1', 'PCA2'])
pca_df['Cluster'] = clusters

plt.figure(figsize=(12, 8))
colors = ['purple', 'blue', 'green', 'yellow']
for i in range(4):
    mask = pca_df['Cluster'] == i
    plt.scatter(pca_df[mask]['PCA1'], pca_df[mask]['PCA2'], 
                label=f'Cluster {i}', alpha=0.6, s=50, color=colors[i])
plt.title('PCA of Customer Segments', fontsize=14, fontweight='bold')
plt.xlabel(f'PCA Component 1 ({pca.explained_variance_ratio_[0]:.1%} variance)', fontsize=12)
plt.ylabel(f'PCA Component 2 ({pca.explained_variance_ratio_[1]:.1%} variance)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reports/figures/pca_clusters.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: reports/figures/pca_clusters.png")

# 3. Cluster Heatmap
print("Generating Cluster Heatmap...")
data['Cluster'] = clusters
cluster_profiles = data.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean()

plt.figure(figsize=(10, 6))
sns.heatmap(cluster_profiles.T, annot=True, fmt='.2f', cmap='coolwarm', 
            cbar_kws={'label': 'Scaled Value'}, linewidths=0.5)
plt.title('Cluster Profiles Heatmap', fontsize=14, fontweight='bold')
plt.xlabel('Cluster', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.tight_layout()
plt.savefig('reports/figures/cluster_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: reports/figures/cluster_heatmap.png")

# 4. Customer Distribution
print("Generating Customer Distribution...")
cluster_counts = data['Cluster'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
colors_bar = ['purple', 'blue', 'green', 'yellow']
bars = plt.bar(cluster_counts.index, cluster_counts.values, color=colors_bar, alpha=0.7, edgecolor='black', linewidth=1.5)
plt.title('Customer Distribution Across Clusters', fontsize=14, fontweight='bold')
plt.xlabel('Cluster', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(range(4))
plt.grid(axis='y', alpha=0.3)

# Add count labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('reports/figures/cluster_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: reports/figures/cluster_distribution.png")

# 5. Total Spent Distribution
print("Generating Total Spent Distribution...")
# Load raw data for spending
raw_data = pd.read_csv('data/raw/online_retail.csv', encoding='latin-1')
raw_data['TotalSpent'] = raw_data['Quantity'] * raw_data['UnitPrice']
total_spent_clean = raw_data['TotalSpent'].dropna()
total_spent_clean = total_spent_clean[total_spent_clean > 0]

plt.figure(figsize=(12, 6))
plt.hist(total_spent_clean, bins=50, color='steelblue', alpha=0.7, edgecolor='black')
plt.title('Distribution of Total Spent per Transaction', fontsize=14, fontweight='bold')
plt.xlabel('Total Spent (£)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('reports/figures/total_spent_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: reports/figures/total_spent_distribution.png")

print("\n✅ All visualizations exported successfully!")
print("Files saved to: reports/figures/")
