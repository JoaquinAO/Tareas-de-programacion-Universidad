# -*- coding: utf-8 -*-
'''
Created on Tue Apr 28 09:31:40 2020

@author: joaquin


    
largo = input("Introduce el largo\n")
ancho = input("Introduce el ancho\n")
    
if largo == ancho:
    print("Es un cuadrado")
else:
    print("Es un rectángulo")'''


numeros=[]
impares=[]
i=0

while i !=10:
  while True:
    try:
      numero = int(input("Introduzca valor para el número " + str(i + 1) + ": " ))
      if numero>0:
        break
      else:
        print("Carácter inválido, por favor introduzca un número entero positivo")
    except:
      print("Carácter inválido, por favor introduzca un número entero")
  numeros.append(numero)
  i=i+1
numeros.sort(reverse=True)

for j in range(0,len(numeros)-1):
  if numeros[j]%2 != 0:
    impares.append(numeros[j])

print("RESULTADOS FINALES")    
print("")
print("El valor más pequeño es:", numeros[len(numeros)-1])
print("")
print("La suma de los valores impares es:",sum(impares)+1)
print("")
for i in range(0,len(numeros)-1):
  if numeros[i]!=numeros[i+1]:
    print("Los dos valores mas grandes son", numeros[i], "y", numeros[i+1])
    break
        