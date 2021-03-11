#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
x = iris.data
y = iris.target

#print(x.shape)
#plt.scatter (x[:,0], x[:,1], c=y, alpha=0.8)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 5)
#random pour fixer

model= KNeighborsClassifier()
model.fit(x_train, y_train)

#cross_val_score(KNeighborsClassifier(), x_train, y_train, cv=5, scoring='accuracy').mean()

#faire une boucle for pour changer les nbre de voisin 
val_score = []
for k in range (1, 50):
    score = cross_val_score(KNeighborsClassifier(k), x_train, y_train, cv=5, scoring='accuracy').mean()
    val_score.append(score)
plt.plot(val_score)
    
    





