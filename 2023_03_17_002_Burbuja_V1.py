# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:44:22 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def Burbuja(arr):
    n = len(arr)
    
    # Iterar a través de todos los elementos del arreglo
    for i in range(n):
        
        # Last i elementos ya están en su lugar correcto
        for j in range(0, n-i-1):
            
# Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

#
arr = [64, 34, 25, 12, 22, 11, 90]
Burbuja(arr)
print ("El arreglo ordenado es:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
