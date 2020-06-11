#Desarrolle un algoritmo en Python que a partir de la lectura de dos datos numéricos enteros
#(largo y ancho), determine e informe si corresponden a un cuadrado o un rectángulo. 
#Incorpore mensajes para orientar al usuario del programa. 


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




    
