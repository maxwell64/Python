import matplotlib.pyplot as graph
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

np.set_printoptions(precision=5, suppress=True)
# Suppressing scientific float notation
np.random.seed(4711)

# Generate 2 clusters: a with 100 points, b with 50
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100])
# Draw random samples from a multivariate normal distribution
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50])
# The multivariate normal distribution is a generalisation of the 2D normal
# distribution to higher dimensions
X = np.concatenate((a, b),)
print(X.shape)  # Should be 150 samples with 2 dimensions

# Generate the linkage matrix
graph.scatter(X[:, 0], X[:, 1])
graph.show()
# Create dendrogram
Z = linkage(X, 'ward')
# Ward is one of the methods that can be used to calulate the distance
# between newly formed clusters. 'ward' causes the linkage to use the Ward
# variance minimisation algorithm
graph.figure(figsize=(10,5))
graph.title('Hierarchical Clustering Dendrogram')
graph.xlabel('sample index')
graph.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,
    leaf_font_size=8.,
)

graph.savefig('clustering_dendrogram.png')
graph.show()
