archivo = open("C:\\Users\\joaquin\\Desktop\\U\\Algoritmos y programación\\Tareas\\Tarea 08\\FilaBanco.txt", "r")
temperatura2 = None 
temperatura3 = None
for linea in archivo:
    datos = linea.split(",")
    temperatura = float(datos[2])
    #Condición para mostrar en pantalla quién debe ser notificado como presunto contagiado
    if temperatura2 != None and temperatura3 != None:
        if temperatura3 > 37.5 and temperatura > 37.5 and temperatura2 <= 37.5:
            print(nombre, apellido)
    temperatura3 = temperatura2 
    temperatura2 = temperatura 
    nombre = datos[0]
    apellido = datos [1]
archivo.close()