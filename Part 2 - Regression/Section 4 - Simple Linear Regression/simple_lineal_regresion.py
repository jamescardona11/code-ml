#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:07:46 2020

@author: zoro
"""

#Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data set

dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


#Split dataset in two subset 'Testing' and 'Training'
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3,random_state = 0)

#Scaling values
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
#"""

#Create a simple regression model for train subset
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train)

# Use the test subset
y_pred = regression.predict(x_test)

#creat a plot to see data train
plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, regression.predict(x_train), color = "blue")
plt.title("Salary vs Time of Experience")
plt.xlabel("Time of Expereience")
plt.ylabel("Salary $")
plt.show()


#creat a plot to see data test
plt.scatter(x_test, y_test, color="red")
plt.plot(x_train, regression.predict(x_train), color = "blue")
plt.title("Salary vs Time of Experience")
plt.xlabel("Time of Expereience")
plt.ylabel("Salary $")
plt.show()