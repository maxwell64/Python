import numpy as np
import matplotlib.pyplot as graph
from matplotlib import style
style.use('ggplot')
from sklearn.cluster import KMeans

# Create data
x = np.array(
    [
        [1, 2],
        [5, 8],
        [1.5, 1.8],
        [8, 8],
        [1, 0.6],
        [9, 11]
    ])

# Initialise kmeans to be the KMeans algorithm with the required number of
# clusters
kmeans = KMeans(n_clusters=2)
# fit() to fit the data i.e. do the learning
kmeans.fit(x)
# Grab the data for the centroids and the labels of the fitted data
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

# Now to plot and visualise the findings based on our data and the fitting
# according to the number of clusters we specified

colors = ['r.', 'g.', 'y.', 'c.']

for i in range(len(x)):
    print('coordinate: ', x[i], 'label: ', labels[i])
    graph.plot(x[i][0], x[i][1], colors[labels[i]], markersize=10)

graph.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=150, linewidth=5,
zorder=10)
graph.show()
