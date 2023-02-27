"""
Estructura de control que me permitee controlar el flujo del programa
Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones

SI NO:
    Se ejecutan otro grupo de instrucciones

en Python


if condicion:
    instrucciones
else:
    otras instrucciones

"""

# Ejemplo 1

print("######### EJEMPLO 1 ##########")

color = "rojo"
# Operador de comparación ==
color = input("Adivina cual es mi color favorito: ")
if color == "rojo":
    print("El color es ROJO")
else:
    print("Color incorrecto!!")

print("\n########## EJEMPLO 2 #########")

# year = 2021 #Variable que me compare el año
year = int(input("¿En que año estamos? "))
if year >= 2022:
    print("Estamos de 2022 en adelante!!")
else:
    print("Es un año anterior al 2022")


print("\n########## EJEMPLO 3 ##########")

nombre = "Andrés Guzmán"
ciudad = "Popayán"
continente = "America del sur"
edad = 36
mayoria_edad = 18

if edad >= mayoria_edad:
    #instrucciones
    print(f"{nombre} es mayor de edad!!")
    if continente != "America del sur":
        print("el usuario No es Americano")
    else:
        print(f"Es americano y de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")


print("\n########## EJEMPLO 4 ##########")

dia = int(input("Intrduce el número del día de la semana: "))

if dia == 1:
    print("es lunes")
else:
    if dia == 2:
        print("es martes")
    else:
        if dia == 3:
            print("es miercoles")
        else:
            if dia == 4:
                print("es Jueves")
            else:
                if dia == 5:
                    print("es viernes")
                else:
                    if dia == 6:
                        print("es sábado")
                    else:
                        if dia == 7:
                            print("es domingo")

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sábado")
elif dia == 7:
    print("Es domingo")

print("\n############ EJEMPLO 5 ###########")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("¿Tienes edad de trabajar? Digite su edad!! "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Está en edad de trabajar!!")
else:
    print("NO está en edad de trabajar!!")


print("\n########### EJEMPLO 7 ##########")

pais = "Colombia"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} No es un país de habla hispana!!")
else:
    print(f"{pais} Sí es un país de habla hispana!!")

print("\n############ EJEMPLO 8 ###########")

pais = "España"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} No es un país de habla hispana!!")
else:
    print(f"{pais} Sí es un país de habla hispana!!")