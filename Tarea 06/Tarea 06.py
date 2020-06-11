mayor1 = -1
mayor2 = -1
menor = 1000000000000000
numerosImpares = 0

print('''Este programa comprara los números ingresados y encuentra:
- El menor número ingresado
- La suma de los números impares ingresados
- Los dos números mayores ingresados
''')



#Ciclo para poder ingresar los 50 números
for i in range(50):
    #Validación de datos

    while True:
        try:
            numero = int(input("Digite los números a comparar: "))
            if numero < 0:
                raise ValueError("Ingrese solo números enteros positivos")
            break
        except ValueError:
            print("Ingrese solo números enteros positivos")
    #Encuentra el primer mayor
    if numero > mayor1:
        mayor2 = mayor1
        mayor1 = numero
    
    #Encuentra el segundo mayor
    elif numero > mayor2:
        mayor2 = numero
    
    #Encuentra el menor
    if numero < menor:
        menor = numero
    
    #Suma de los números impares
    if numero % 2 !=0:
        numerosImpares += numero
    
print("")
print("El número menor es", menor)
print("La suma de los números impares es", numerosImpares)
print("El número mayor es", mayor1, "y el segundo mayor es", mayor2)
