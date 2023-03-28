# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:46:24 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def countingSort(arr):
    # Encontrar el rango de valores en el arreglo
    max_val = max(arr)
    # Contar la frecuencia de cada valor en el arreglo
    count_arr = [0] * (max_val + 1)
    for x in arr:
        count_arr[x] += 1
    # Calcular la posición final de cada valor en el arreglo ordenado
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    # Construir el arreglo ordenado
    sorted_arr = [0] * len(arr)
    for x in arr:
        sorted_arr[count_arr[x]-1] = x
        count_arr[x] -= 1
    return sorted_arr

#
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = countingSort(arr)
print("El arreglo ordenado es:")
for i in range(len(sorted_arr)):
    print("%d" % sorted_arr[i])
