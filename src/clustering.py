from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import pandas as pd

def perform_kmeans_clustering(data, n_clusters):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(scaled_data)

    labels = kmeans.labels_
    silhouette_avg = silhouette_score(scaled_data, labels)

    return labels, silhouette_avg

def perform_dbscan_clustering(data, eps, min_samples):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(scaled_data)

    return labels

def add_cluster_labels_to_data(data, labels, algorithm='KMeans'):
    data['Cluster'] = labels
    return data

def evaluate_clustering(labels, data):
    silhouette_avg = silhouette_score(data, labels)
    return silhouette_avg