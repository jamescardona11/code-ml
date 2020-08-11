#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:57:15 2020

@author: zoro
"""

#Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data set

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#remove nan data from dataset
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[:, 1:3])

x[:, 1:3] = imputer.transform(x[:, 1:3])

#coding category var in dataset

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelEncoder_X = LabelEncoder()
x[:, 0] = labelEncoder_X.fit_transform(x[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
x = onehotencoder.fit_transform(x).toarray()

labelEncoder_Y = LabelEncoder()
y = labelEncoder_Y.fit_transform(y)


#Split dataset in two subset 'Testing' and 'Training'
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2,random_state = 0)