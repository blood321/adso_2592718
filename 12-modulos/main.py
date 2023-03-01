"""
Modulos: son funciones ya hechas para reutilizar.
"""
#Importar Modulo propio
import mimodulo

print(mimodulo.holaMundo("Carlos Gómez"))
print(mimodulo.calculadora(3, 5, True))
print("---------------------------------")
#Otra forma de llamar el modulo
from mimodulo import holaMundo
print(holaMundo("Juan Perez"))
print("----------------------------------")
#llamas todas las funciones de mi modulo
from mimodulo import *
print(holaMundo("Sandra Sánchez"))
print(calculadora(8,4,True))

# Modulo fechas
print("Modulo fechas")
print("-----------------------------------")
import datetime
print(datetime.date.today())

# Fecha completa con tiempo
print("fecha completa con tiempo")
print("-----------------------------------")
fecha_completa = datetime.datetime.now()
print(fecha_completa)

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H%M%S")
print(f"Mi fecha personalizada: {fecha_personalizada}")

print("---------------------------------------")
# Modulo matemáticas
print("Modulo matemáticas")
import math
print("Raiz cuadrada de 10", math.sqrt(10))
print("Número PI: ", math.pi)
print("Redondear",math.ceil(5.34562))
print("Redondear",math.floor(5.34562))

print("Modulo Random")
import random
print("Número aleatorio entre 15 y 67 ", random.randint(15, 67))
