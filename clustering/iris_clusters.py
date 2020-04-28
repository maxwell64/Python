import numpy as np
import matplotlib.pyplot as graph
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)
centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
X = iris.data  # X coords
y = iris.target  # Y coords

# Making an array where we init 3 kmeans cluster algorithms
# First make 3 clusters
# Seconds make 8 clusters
# Lastly create a random cluster

estimators = {'k_means_iris_3': KMeans(n_clusters=3),
    'k_means_iris_8': KMeans(n_clusters=8),
    'k_means_iris_bad_init': KMeans(n_clusters=3, n_init=1,
    init='random')}

fignum = 1
for name, est in estimators.items():
    fig = graph.figure(fignum, figsize=(4, 3))  # Create a 4x3 figure
    graph.cla()  # Clear the current figure
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)  # Create rectangle
    graph.cla()  # Clear all axes
    est.fit(X)  # Set x values in output plot
    labels = est.labels_

    ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels.astype(np.float))
    # Make our values scatter X[:, 3] => values up to 3
    ax.w_xaxis.set_ticklabels([])  # Set text values for tick labels
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Petal width')  # Set axis labels
    ax.set_ylabel('Sepal length')
    ax.set_zlabel('Petal length')
    fignum += 1

# Plot the x and y axes without clustering
fig = graph.figure(fignum, figsize=(4, 2))
graph.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
graph.cla()

for name, label in [
    ('Setosa', 0),
    ('Versicolour', 1),
    ('Virginica', 2)]:
    # Set labels
    ax.text3D(X[y == label, 3].mean(),
        X[y == label, 0].mean() + 1.5,
        X[y == label, 2].mean(), name,
        horizontalalignment='center',
        bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))

# Reorder labels to match colurs to cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=y)

# Another plot
ax.w_xaxis.set_ticklabels([])  # Set text values for tick labels
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('Petal width')  # Set axis labels
ax.set_ylabel('Sepal length')
ax.set_zlabel('Petal length')
graph.savefig('iris_clustering.png')
graph.show()
