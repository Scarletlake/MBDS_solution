# Q3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

# Read data from input file
test_data_x = pd.read_csv("test_data.txt", sep='\t')
data_x = pd.read_csv("train_data.txt", sep='\t')
data_y = pd.read_csv("train_truth.txt")

# Preparing the data

scale = StandardScaler(with_mean=True,with_std=True)
data_x = scale.fit_transform(data_x)

train_x,test_x,train_y,test_y = train_test_split(data_x,data_y,test_size = 0.2,random_state = 1)

# Construct the MLP modle

#  4x4 hidden layers
mlp_reg = MLPRegressor(hidden_layer_sizes=(4,4), 
                    activation='tanh', 
                    solver='adam', 
                    alpha=0.0001,   
                    max_iter=100, 
                    random_state=12,
                   )

mlp_reg.fit(train_x,train_y.values.ravel())

# predict using test data
predict_y = mlp_reg.predict(test_data_x)
  
# Print the results to outputfile
# Converting the float number to exponential number 
results = pd.DataFrame(["{:e}".format(y) for y in predict_y],columns=['y'], )
results.to_csv("test_predicted.txt", index=0)


