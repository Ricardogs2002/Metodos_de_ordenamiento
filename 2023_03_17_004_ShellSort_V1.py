# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:21:34 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def shellSort(arr):
    # Inicializar la brecha más grande
    n = len(arr)
    gap = n // 2
    
    # Reducir la brecha en cada iteración hasta que sea 1
    while gap > 0:
#Realizar la inserción de brecha para todos los elementos con 
#índices mayores a la brecha actual
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
#Mover los elementos del arreglo que son mayores que el elemento de la 
#brecha anterior a una posición adelante en el arreglo con brecha actual
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
# Insertar el elemento de la brecha anterior en su lugar 
#correcto en el arreglo con brecha actual
            arr[j] = temp
        
        # Reducir la brecha para la siguiente iteración
        gap //= 2

#
arr = [64, 34, 25, 12, 22, 11, 90]
shellSort(arr)
print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i])
