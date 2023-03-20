# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:00:59 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def Insercion(arr):
    # Recorrer todos los elementos del arreglo
    for i in range(1, len(arr)):
        key = arr[i]
        
# Mover los elementos que son mayores que la clave a una posición adelante
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 
arr = [64, 34, 25, 12, 22, 11, 90]
Insercion(arr)
print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i])
