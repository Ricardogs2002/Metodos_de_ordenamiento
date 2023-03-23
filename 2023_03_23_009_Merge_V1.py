# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:09:43 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def mergeSort(arr):
    if len(arr) > 1:
 
# Dividir el arreglo en dos mitades
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
 
# Llamada recursiva a mergeSort() para las dos mitades
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0

# Copiar los elementos de L y R en el arreglo original
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
# Copiar los elementos restantes de L y R en el arreglo original
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
#
arr = [64, 34, 25, 12, 22, 11, 90]
mergeSort(arr)
print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i])
