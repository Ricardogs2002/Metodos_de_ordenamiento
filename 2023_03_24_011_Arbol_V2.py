# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:36:41 2023

@author: Ricardo Ismael Gomez Sanchez
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.valor < nodo.valor:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.valor)
        inorden(raiz.derecha)

def ordenamiento_de_arbol(arr):
    raiz = Nodo(arr[0])
    for i in range(1, len(arr)):
        insertar(raiz, Nodo(arr[i]))
    inorden(raiz)

arr = [64, 34, 25, 12, 22, 11, 90]
print("El arreglo ordenado es:")
ordenamiento_de_arbol(arr)