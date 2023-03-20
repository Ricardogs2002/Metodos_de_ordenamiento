# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:07:51 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def Seleccion(arr):
    # Recorrer todos los elementos del arreglo
    for i in range(len(arr)):
        # Encontrar el elemento mínimo restante en el arreglo
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
# Intercambiar el elemento mínimo encontrado con el primer elemento sin ordenar
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#
arr = [64, 34, 25, 12, 22, 11, 90]
Seleccion(arr)
print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i])
