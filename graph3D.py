#graphique 3d avec poo
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D

iris = load_iris()
x = iris.data
y = iris.target 
names = list(iris.target_names)

ax = plt.axes(projection='3d')# on creé un objet axe avec la fct axes 
ax.scatter(x[:,0],x[:,1],x[:,2],c=y)

plt.show()
