#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:01:00 2024

@author: emmanuel
"""

def bubble(array):
    n = len(array)
    
    for i in range(n-1):
        for j in range (n-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1], array[j]
                
elementos = [8,3,1,19,14]
bubble(elementos)

print (elementos)