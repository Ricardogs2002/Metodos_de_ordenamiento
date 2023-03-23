# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:36:41 2023

@author: Ricardo Ismael Gomez Sanchez
"""
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

# Función para insertar un nuevo nodo en el árbol
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# Función para recorrer el árbol en orden y agregar los valores a un arreglo
def inorderTraversal(root, res):
    if root:
        inorderTraversal(root.left, res)
        res.append(root.val)
        inorderTraversal(root.right, res)

# Función principal de ordenamiento por árbol
def treeSort(arr):
    root = None
    # Insertar cada elemento del arreglo en el árbol
    for i in range(len(arr)):
        insert(root, Node(arr[i]))
    res = []
    # Recorrer el árbol en orden y agregar los valores a un arreglo
    inorderTraversal(root, res)
    return res

# Ejemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = treeSort(arr)
print("El arreglo ordenado es:")
for i in range(len(sorted_arr)):
    print("%d" % sorted_arr[i])