import pandas as pd

#the url for the dataset and describes the names of the columns
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']

#imports the data from the url and puts it in a dataframe
data = pd.read_csv(url, names = names, index_col = False)

#print the first 5 rows of data
print('\nThe first 5 rows of the data:\n', data.head())

#print the shape of the dataset
print('\nThe shape of the dataset:', data.shape)

print('\nDescriptive statistics:')
#how much data to show, corresponds to width of console
pd.set_option('display.width', 100)
#how many decimal places to use
pd.set_option('precision', 3)
#prints a description of the dataset, including the total amount of data, the mean values, and the standard deviation
print(data.describe())

print('\nCorrelation between attributes:')
#Finds relationships between values; 0 == no relation, +/-1 == fully related
correlations = data.corr(method = 'pearson')
print(correlations)

print('\nSkew for data')
#Finds the skew of the dataset attributes
skew = data.skew()
print(skew)
