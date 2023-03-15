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

import sys

clave = int(input("Ingresa un clave del 1 al 6: "))
matPrima = int(input("Ingresa el valor de la materia prima: "))

if clave == 3 or clave == 4:
    manoObra = matPrima * 75/100
elif clave == 1 or clave == 5:
    manoObra = matPrima * 80/100
elif clave == 2 or clave == 6:
    manoObra = matPrima * 85/100
else:
    print("La clave no es correcta")
    sys.exit()

if clave == 2 or clave == 5:
    gasFabri = matPrima * 30/100
elif clave == 3 or clave == 6:
    gasFabri = matPrima * 35/100
elif clave == 1 or clave == 4:
    gasFabri = matPrima * 28/100

cosPro = matPrima + manoObra + gasFabri
precioVenta = cosPro * 0.45 + cosPro
print(f"El precio de venta es {precioVenta}")