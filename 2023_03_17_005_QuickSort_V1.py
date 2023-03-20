# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:20:35 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def quickSort(arr, low, high):
    if low < high:
        # Encontrar el índice de partición
        pi = partition(arr, low, high)
 
        # Ordenar los elementos antes y después del índice de partición
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
 
def partition(arr, low, high):
    # Elegir el pivote como el elemento más a la derecha
    pivot = arr[high]
 
    # Establecer el índice de la pared
    i = low - 1
 
    # Recorrer todos los elementos del arreglo
    for j in range(low, high):
        # Si el elemento actual es menor o igual que el pivote,
        # moverlo al lado izquierdo de la pared
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
 
# Intercambiar el pivote con el elemento a la derecha de la pared
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
 
#
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
quickSort(arr, 0, n-1)
print("El arreglo ordenado es:")
for i in range(n):
    print("%d" % arr[i])
