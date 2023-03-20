# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:25:44 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def heapSort(arr):
    n = len(arr)

    # Construir un max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer los elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el máximo actual con el último elemento
        heapify(arr, i, 0)  # Llamar a heapify en el heap reducido

def heapify(arr, n, i):
    largest = i  # Inicializar el nodo raíz como el más grande
    left = 2 * i + 1  # Izquierda = 2*i + 1
    right = 2 * i + 2  # Derecha = 2*i + 2

    # Verificar si el hijo izquierdo del nodo es mayor que el nodo raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verificar si el hijo derecho del nodo es mayor que el nodo raíz
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Cambiar la raíz si es necesario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Ejemplo de uso:
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("El arreglo ordenado es:")
for i in range(n):
    print("%d" % arr[i])
