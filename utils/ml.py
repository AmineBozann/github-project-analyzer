from sklearn.cluster import KMeans
import numpy as np

def apply_kmeans(projects):
    data = []

    for p in projects:
        data.append([
            p['stars'],
            p['forks'],
            p['issues'],
            p['score']
        ])

    X = np.array(data)

    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)

    for i, p in enumerate(projects):
        p['cluster'] = int(labels[i])

    return projects