# precioInicial = int(input("Precio inicial kilo de Uva: "))
# tipoUva = input("Ingrese el tipo de uva 'a' o 'b': ")
# tamUva = int(input("Ingresa el tamaño 1 o 2: "))
# kilo = int(input("kilos: "))

# if tipoUva == "a" and tamUva == 1:
#     precioInicial += 200
# elif tipoUva == "a" and tamUva == 2:
#     precioInicial += 300
# elif tipoUva == "b" and tamUva == 1:
#     precioInicial -= 300
# elif tipoUva == "b" and tamUva == 2:
#     precioInicial -= 500
# else:
#     print("Los valores que digitaste no se encuentran")

# ganancia = precioInicial * kilo
# print(ganancia)

'''
Ejercicio costos de producción
'''

# import sys

# clave = int(input("Ingresa un clave del 1 al 6: "))
# matPrima = int(input("Ingresa el valor de la materia prima: "))

# if clave == 3 or clave == 4:
#     manoObra = matPrima * 75/100
# elif clave == 1 or clave == 5:
#     manoObra = matPrima * 80/100
# elif clave == 2 or clave == 6:
#     manoObra = matPrima * 85/100
# else:
#     print("La clave no es correcta")
#     sys.exit()

# if clave == 2 or clave == 5:
#     gasFabri = matPrima * 30/100
# elif clave == 3 or clave == 6:
#     gasFabri = matPrima * 35/100
# elif clave == 1 or clave == 4:
#     gasFabri = matPrima * 28/100

# cosPro = matPrima + manoObra + gasFabri
# precioVenta = cosPro * 0.45 + cosPro
# print(f"El precio de venta es {precioVenta}")

'''
Ejercicio con descuentos en productos de dulceria
'''

# cantidadDulce = int(input("Ingrese la cantidad de dulces a comprar: "))
# tipoDulce = int(input("Ingrese tipo de dulce [1, 2 o 3]: "))
# precioUni1 = 3.0
# precioUni2 = 4.0
# precioUni3 = 5.0

# print(f"Tipo de dulce: {tipoDulce}")

# if tipoDulce == 1:
#     if cantidadDulce <= 5:
#         print(f"Precio Unitario: {precioUni1}")
#         precioUni1 -= precioUni1 * 0.5
#         monto = cantidadDulce * precioUni1
#     elif cantidadDulce > 5 < 10:
#         print(f"Precio Unitario: {precioUni1}")
#         precioUni1 -= precioUni1 * 0.07
#         monto = cantidadDulce * precioUni1
# elif tipoDulce == 2:
#     if cantidadDulce < 7:
#         print(f"Precio Unitario: {precioUni2}")
#         precioUni2
#         monto = cantidadDulce * precioUni2
#     elif cantidadDulce > 7:
#         print(f"Precio Unitario: {precioUni2}")
#         precioUni2 -= precioUni2 * 0.05
#         monto = cantidadDulce * precioUni2
# elif tipoDulce == 3:
#     if cantidadDulce <= 4:
#         print(f"Precio Unitario: {precioUni3}")
#         precioUni3
#         monto = cantidadDulce * precioUni3
#     else:
#         precioUni3 -= precioUni3 * 0.15
#         monto = cantidadDulce * precioUni3

# print(f"Cantidad de dulces: {cantidadDulce}")
# print(f"Monto de venta: {monto}")


'''
Ejemplo diccionarios
'''

# dicc = {}
# dicc["Nombre"] = input("Ingrese el nombre: ")
# dicc["Edad"] = int(input("Ingrese la edad: "))
# dicc["Cédula"] = int(input("Ingrese la Cédula: "))
# sexo = input("Ingrese F para femenino o M para masculino: ")

# if sexo == "f":
#     dicc["Sexo"] = "Femenino"
# else:
#     dicc["Sexo"] = "Masculino"

# print(dicc)

def promedioTrabajos(nombre):
    a = int(input("ingresa la nota del lunes: "))
    b = int(input("ingresa la nota del martes: "))
    c = int(input("ingresa la nota del miercoles: "))
    d = int(input("ingresa la nota del jueves: "))
    e = int(input("ingresa la nota del viernes: "))
    factor = (a + b + c + d + e) * 0.25
    prom = (a + b + c + d + e) / 5
    return print(f"El Factor de trabajos subido fue {factor} y el promedio de los trabajos subidos por semana de {nombre} fue: {prom}")

promedioTrabajos(nombre = input("Ingresa el nombre: "))