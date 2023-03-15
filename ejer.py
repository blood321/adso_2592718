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
    matPrima += matPrima*75/100
    manoObra = matPrima
elif clave == 1 or clave == 5:
    matPrima += matPrima*80/100
    manoObra = matPrima
elif clave == 2 or clave == 6:
    matPrima += matPrima*85/100
    manoObra = matPrima
else:
    print("La clave no es correcta")
    sys.exit()

if clave == 2 or clave == 5:
    matPrima += matPrima * 0.30
    gasFabri = matPrima
elif clave == 3 or clave == 6:
    matPrima += matPrima * 0.35
    gasFabri = matPrima
elif clave == 1 or clave == 4:
    matPrima += matPrima * 0.28
    gasFabri = matPrima

cosPro = matPrima + manoObra + gasFabri
precioVenta = cosPro + cosPro * 0.45
print(f"El precio de venta es {precioVenta}")