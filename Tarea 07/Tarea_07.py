#Joaquín Aravena O'Brien

archivo = open("Secuencia_1.txt", "r")
valor = 1000
contadorSecuencias = 0

for linea in archivo:

    datos = linea.split()

    num = int(datos[0])

    if num < valor:
        valor = num
        contadorSecuencias += 1
    else:
        valor = num

archivo.close()
print("")
print("Existen", contadorSecuencias, "secuencias ascendentes en el archivo")

