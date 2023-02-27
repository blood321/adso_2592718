"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la función cuantas veces como sea necesario. Ejemplo de sintaxis:

def nombreDeMiFuncion(parametros):
    #bloque de código / conjunto de instrucciones
#invocar
nombreDeMiFuncion(mi_parametro)
"""

# Ejemplo 1

print("\n########## Ejemplo 1 ##########")
# Definir función
# def muestraNombre():
#     print("Victor")
#     print("Pedro")
#     print("Juan")
#     print("Felipe")
#     print("Santiago")
#     print("Sandra")
# # Invocar función
# muestraNombre()

# Ejemplo 2 - Parametros
print("\n########## Ejemplo 2 PARAMETROS #########")

# def mostrarTuNombre(nombre): #parametro
#     print(f"Tu nombre es: {nombre}")
# nombre = input("Introduce tu nombre: ")
# mostrarTuNombre(nombre)

# def mostrarTuNombreYEdad(nombre, edad): #parametro
#     print(f"Tu nombre es: {nombre}")
#     if edad >= 18:
#         print(f"Y eres mayor de edad")

# nombre = input("Introduce tu nombre: ")
# mostrarTuNombreYEdad(nombre, 19)

print("\n########## Ejemplo 3 Parametros Tablas de Multiplicar #########")

# def tabla(numero):
#     print(f"Tabla de multiplicar del número: {numero}")

#     for contador in range(5):
#         operacion = numero * contador
#         print(f"{numero} X {contador} = {operacion}")

#     print("\n") #salto de línea

# tabla(int(input("Elige el número de tabla: ")))
# tabla(14)

# # Ejemplo 4 - Parametros Opcionales
# print("########## Ejemplo 4 Parametros opcionales  ########")
# def getEmpleado(nombre, dni = None):
#     print("EMPLEADO")
#     print(F"Nombre: {nombre}")
#     if dni != None:
#         print(f"DNI: {dni}")

# getEmpleado("Andrés Guzmán", 1061692813)

# Ejemplo 5 - Parametros Opcionales y return o devolver datos de una función
# print("########## Ejemplo 5 Parametros Opcionales y return o devolver datos de una función ######")
# def calculadora(numero1, numero2, basicas = False):
#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multiplicacion = numero1 * numero2
#     division = numero1 / numero2
#     cadena = ""
#     cadena += "Suma: " + str(suma)
#     cadena += "\n"
#     cadena += "Resta: " + str(resta)
#     cadena += "\n"
#     cadena += "Multiplicación: " + str(multiplicacion)
#     cadena += "\n"
#     cadena += "División: " + str(division)
#     cadena += "\n"
#     return cadena
# print(calculadora(5, 5))

# Ejemplo 5 - Parametros Opcionales y return o devolver datos de una función
print("\n###### Ejemplo 5 Parametros Opcionales y return o devolver datos de una función #####")
# def calculadora(numero1, numero2, basicas = False):
#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multiplicacion = numero1 * numero2
#     division = numero1 / numero2
#     cadena = ""
#     if basicas != False:
#         cadena += "Suma: ", str(suma)
#         cadena += "\n"
#         cadena += "Resta: ", str(resta)
#         cadena += "\n"
#     else:
#         cadena += "Multiplicación: " + str(multiplicacion)
#         cadena += "\n"
#         cadena += "División: " + str(division)
#         cadena += "\n"
#     return cadena
# print(calculadora(int(input("ingresa numero 1: ")),int(input("ingresa numero 2: "))))
        
# Ejemplo 6 - Uso de funciones dentro de una función
print("######### Ejemplo 6 Funciones dentro de una función ######")

# def getNombre(nombre):
#     texto = f"El nombre es: {nombre}"
#     return texto

# def getApellido(apellido):
#     texto = f"El apellido es: {apellido}"
#     return texto
# print(getNombre("Carlos"), getApellido("Sanchez"))

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devolverTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto
print(devolverTodo("José", "Pérez"))

# Ejemplo 7 - función Lambda

print("####### Ejemplo 7 Función Lambda #####")

dime_el_year = lambda year: f"El año es {year}"
print(dime_el_year(2023))