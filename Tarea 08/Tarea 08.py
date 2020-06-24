archivo = open("FilaBanco.txt", "r")

for linea in archivo:
    
    datos = linea.split(",")

    nombre = datos[0]
    apellido = datos[1]
    temperatura = float(datos[2])
    print(nombre, apellido, temperatura)
    #Verificar que siempre hayan más de tres personas

    #Condición para mostrar en pantalla quién debe ser notificado como presunto contagiado
    
    #Condición para no contar a una persona con temperatura mayor a 37.5 (porque ya se considera contagiada)
    
archivo.close()