# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:35:18 2023

@author: Familia Gomez Sanche
"""

def Cocktail(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        # Mover los elementos más grandes al final
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        # Mover los elementos más pequeños al inicio
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1

#
arr = [5, 3, 8, 6, 7, 2]
Cocktail(arr)
print("Lista ordenada:")
print(arr)
