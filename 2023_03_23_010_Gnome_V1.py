# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:30:20 2023

@author: Ricardo Ismael Gomez Sanchez
"""
def GnomeSort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr

#
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = GnomeSort(arr)
print("El arreglo ordenado es:")
for i in range(len(sorted_arr)):
    print("%d" % sorted_arr[i])
