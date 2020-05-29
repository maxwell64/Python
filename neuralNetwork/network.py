import numpy as np
from dlnet import dlnet
import pandas as pd
import matplotlib.pyplot as graph
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import itertools

data = pd.read_csv('breast-cancer-wisconsin.data', header=None)
data.iloc[:, 10].replace(2, 0, inplace=True)
data.iloc[:, 10].replace(4, 1, inplace=True)

data = data[~data[6].isin(['?'])]
data = data.astype(float)

names = data.columns[0:10]
scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(data.iloc[:, 0:10])
scaled_data = pd.DataFrame(scaled_data, columns=names)

print(data.head(5))

x = scaled_data.iloc[0:500, 1:10].values.transpose()
y = data.iloc[0:500, 10:].values.transpose()

xval = scaled_data.iloc[500:, 1:10].values.transpose()
yval = data.iloc[500:, 10:].values.transpose()

nn = dlnet(x, y)
nn.lr = 0.01
nn.dims = [9, 15, 1]

nn.gd(x, y, iter=15000)
pred_train = nn.pred(x, y)
pred_test = nn.pred(xval, yval)
