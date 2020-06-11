isosceles = 0
equilateros = 0
porcentajeEquilateros = 0
areaTotalEquilateros = 0
areaTotalEscalenos = 0
areaTotalIsosceles = 0
triangulos = 0

#Ciclo para pedir los datos de los 10 terrenos triangulares
for i in range(10):
    #Entrada y validación de datos
    while True:
        try:
            a = float(input("Lado A del triángulo " + str(i + 1) + "\n"))
            break
        except ValueError:
            print("Ingresa solo números")

    while True:
        try:
            b = float(input("Lado B del triángulo " + str(i + 1) + "\n"))
            break
        except ValueError:
            print("Ingresa solo números")

    while True:
        try:
            c = float(input("Lado C del triángulo " + str(i + 1) + "\n"))
            break
        except ValueError:
            print("Ingresa solo números")

    while True:
        try:
            base = float(input("Base del triángulo " + str(i + 1) + "\n"))
            break
        except ValueError:
            print("Ingresa solo números")

    while True:
        try:
            altura = float(input("Altura del triángulo " + str(i + 1) + "\n"))
            break
        except ValueError:
            print("Ingresa solo números")

    #Determinar el tipo de triángulo
    if a == b and a == c:
        triangulos +=1
        areaEquilateros = (base * altura) / 2
        #La variable areaTotalEquilateros guarda la suma de todas las áreas
        #de los triángulos equiláteros
        areaTotalEquilateros +=areaEquilateros 
        #Contador de triángulo equiláteros
        equilateros +=1
        porcentajeEquilateros = (equilateros / 10) * 100
        print("El triángulo es equilátero")
        print("")
    
    elif a != b and a != c:
        triangulos +=1
        areaEscalenos = (base * altura) / 2
        #La variable areaTotalEscalenos guarda la suma de todas las áreas
        #de los triángulos escalenos
        areaTotalEscalenos +=areaEscalenos
        print("El triángulo es escaleno y su área es " + str(areaEscalenos) + "m\u00b2")
        print("")
    
    else:
        triangulos +=1
        areaIsosceles = (base * altura) / 2
        #La variable areaTotalIsosceles guarda la suma de todas las áreas
        #de los triángulos isósceles
        areaTotalIsosceles +=areaIsosceles
        #Contador de triángulos isósceles
        isosceles +=1
        print("El triángulo es isósceles")
        print("")

#Suma las áreas de todos los triángulos
areaTotal = areaTotalEquilateros + areaTotalEscalenos + areaTotalIsosceles

if isosceles == 1:
    print("Hay", isosceles ,"triángulo isósceles")
    print("")
else:
    print("Hay", isosceles ,"triángulos isósceles")
    print("")
    
print("El porcentaje de triángulo equiláteros es " + str(porcentajeEquilateros) +"%")
print("")
print("El área total del terreno procesado es " + str(areaTotal) + "m\u00b2")
