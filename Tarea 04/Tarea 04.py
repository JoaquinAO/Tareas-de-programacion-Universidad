#importamos el módulo "math" para calcular la raíz cuadradad y "cmath" para calcular
#la raíz cuadrada de un número imaginario
import math, cmath

print("La ecuación cuadrática es:")
print('ax\u00b2 + bx + c = 0 (recuerda que "a" no puede ser 0)')

a = float(input("Ingrese el valor de a:\n"))
b = float(input("Ingrese el valor de b:\n"))
c = float(input("Ingrese el valor de c:\n"))

discriminante = b**2 - (4 * a * c)

#math.sqrt para obtener la raíz cuadrada
if discriminante > 0:
    sol1 = (-b + math.sqrt(discriminante)) / (2 * a)
    sol2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("La ecuación tiene dos soluciones reales distintas")
    print("Las soluciones son", float(sol1), "y", float(sol2))

if discriminante == 0:
    solución = -b / (2 * a)
    print("La ecuación tiene soluciones reales e iguales")
    print("Las solución es", "y", float(solución))

#cmath.sqrt para obtener la raíz cuadrada de un número imaginario
if discriminante < 0:
    sol1 = ((-b + cmath.sqrt(discriminante)) / (2 * a))
    sol2 = ((-b - cmath.sqrt(discriminante)) / (2 * a)) 
    print('La ecucación tiene dos soluciones complejas conjugadas donde "j" es la unidad imaginaria')
    print("Las soluciones son", sol1, "y", sol2)