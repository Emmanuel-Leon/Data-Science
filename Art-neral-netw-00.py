#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 06:08:46 2024
In this scrip we will a create an artificial neural network 
@author: emmanuel
"""

from scipy import stats

class capa():
    def __init__(self, n_neur_layer_back, n_neur, func_act):
        self.func_act = func_act
        self.b = np.round(stats.truncnorm.rvs(-1,1,loc=0, scale=1, size = n_neur).reshape(1, n_neur),3)
        self.W = np.round(stats.truncnorm.rvs(-1,1,loc=0, scale=1, size = n_neur*n_neur_layer_back).reshape(n_neur_layer_back , n_neur),3)
        
        
import numpy as np
import math 
import matplotlib.pyplot as plt

sigmoid = (
    lambda x:1 / (1 + np.exp(-x)),
    lambda x:x * (1-x)
    )

rango = np.linspace(-10,10).reshape([50,1])
datos_sigmoide = sigmoid[0](rango)
datos_sigmoide_derivada = sigmoid[1](rango)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
axes[0].plot(rango, datos_sigmoide)
axes[1].plot(rango, datos_sigmoide_derivada)
fig.tight_layout()

def derivada_relu(x):
    x[x<=0] = 0
    x[x>0] = 1
    return x

relu = (
        lambda x: x*(x>0),
        lambda x:derivada_relu(x)
        )


datos_relu = relu[0](rango)
datos_relu_derivada = relu[1](rango)

rango = np.linspace(-10,10).reshape([50,1])

plt.cla()
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
axes[0].plot(rango, datos_relu[:, 0])
axes[1].plot(rango, datos_relu_derivada[:, 0])
plt.show()


neuronas = [2,4,8,1]

funciones_act = [relu, relu, sigmoid]

red_neuronal = []

for paso in range(len(neuronas)-1):
    x = capa(neuronas[paso], neuronas[paso+1], funciones_act[paso])
    red_neuronal.append(x)
    
print(red_neuronal)

X = np.round(np.random.rand(20,2),3)

z = X @ red_neuronal[0].W

print(z[:10,:], X.shape, z.shape)

z = z + red_neuronal[0].b

print(z[:5,:])

a = red_neuronal[0].func_act[0](z)
a[:5, :]


output = [X]

for num_capa in range(len(red_neuronal)):
    z = output[-1] @ red_neuronal[num_capa].W + red_neuronal[num_capa].b
    a = red_neuronal[num_capa].func_act[0](z)
    output.append(a)

print (output[-1])    