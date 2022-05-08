#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:33:17 2020

@author: zoro
"""

#Categorical Data

#Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data set

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values



#coding category var in dataset
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelEncoder_X = LabelEncoder()
x[:, 0] = labelEncoder_X.fit_transform(x[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
x = onehotencoder.fit_transform(x).toarray()

labelEncoder_Y = LabelEncoder()
y = labelEncoder_Y.fit_transform(y)