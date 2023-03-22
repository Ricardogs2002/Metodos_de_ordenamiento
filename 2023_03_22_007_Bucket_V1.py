# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:22:33 2023

@author: Familia Gomez Sanche
"""

def Bucket(array):
    # determinar el número de buckets
    num_buckets = 10
    # crear los buckets
    buckets = [[] for _ in range(num_buckets)]
    # distribuir los elementos en los buckets correspondientes
    for i in range(len(arr)):
        bucket_index = int(num_buckets * arr[i])
        buckets[bucket_index].append(arr[i])
    # ordenar cada bucket individualmente
    for i in range(num_buckets):
        buckets[i].sort()
    # concatenar los buckets en un solo array ordenado
    result = []
    for i in range(num_buckets):
        result.extend(buckets[i])
    return result

arr = [0.64, 0.34, 0.25, 0.12, 0.22, 0.11, 0.90]
sorted_arr = Bucket(arr)
print(sorted_arr)
