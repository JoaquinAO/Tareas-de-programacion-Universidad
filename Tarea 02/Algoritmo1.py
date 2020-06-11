# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:31:40 2020

@author: joaquin
"""


print("Programa para saber si tengo un cuadrado o un rectángulo\n")

print("Ingrese solo números enteros")

largo = int(input("Introduce el largo\n"))

while largo < 0:
    print("El largo tiene que ser un número positivo")
    largo = int(input())
    
ancho = int(input("Introduce el ancho\n"))
    
while ancho < 0:
    print("El ancho tiene que ser un número positivo")
    ancho =int(input())

if largo == ancho:
    print("Es un cuadrado")
else:
    print("Es un rectángulo")




    
