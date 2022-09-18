#! python3

'''
Pandas for reading and writing spreadsheets
Numpy for carrying out efficient computations
Matplotlib for visualization of data
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# This is for including plots/graphs inline in a notebook
#%matplotlib inline

# Here is the code for generating some random data in a two-dimensional space:
X = -2 * np.random.rand(100,2) # (100,2) = # of rows, # of columns
X1 = 1 + 2 * np.random.rand(50,2)
X[50:100, :] = X1 # for rows 50 to 100, all columns replace with data from X1
# A total of 100 data points has been generated and divided into two groups, of 50 points each.
# Now show the scatter plot:
plt.scatter(X[ : , 0], X[ : , 1], s = 50, c = 'b')
# X[ : , 0] = first item from every row of the 2D array
# X[ : , 1] = second item from every row of the 2D array
print("Show first plot")
plt.show()

# Process the randomly generated data using K-Means clustering algorithm:
from sklearn.cluster import KMeans
Kmean = KMeans(n_clusters=2) # Instantiate an instance of Kmeans = Kmean.
'''In machine learning, "fitting" means training. The fit function is used for
training of model using data examples. Fit function adjusts weights according
to data values so that better accuracy can be achieved in predictions.'''
Kmean.fit(X)

# We arbitrarily give k (n_clusters)a value of two.
# Create object "array" from class Kmeans
array = KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
 n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
 random_state=None, tol=0.0001, verbose=0)

# Here is the output of the K-means parameters we get if we run the code:'''
# print(array)

'''Finding the centroid
Here is the code for finding the center of the clusters:'''
Kmean.cluster_centers_

'''Let’s display the cluster centroids (using green and red color).'''
plt.scatter(X[ : , 0], X[ : , 1], s =50, c='b')
plt.scatter(-0.94665068, -0.97138368, s=200, c='g', marker='s')
plt.scatter(2.01559419, 2.02597093, s=200, c='r', marker='s')
print("Show second plot")
plt.show()

'''Here is the code for getting the labels property of the K-means clustering
example dataset; that is, how the data points are categorized into the two
clusters.'''
Kmean.labels_

# Lets use the code below for predicting the cluster of a data point:

sample_test=np.array([-3.0,-3.0])
second_test=sample_test.reshape(1, -1)
Kmean.predict(second_test)
