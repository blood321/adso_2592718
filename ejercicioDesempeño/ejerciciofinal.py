import random

print("\nAdivina adivinador un número del 1 al 150 \n")

numAdivinar = random.randint(1, 150)

numUser = int(input("Ingresa tu número: "))
con = 10

while numAdivinar != numUser:
    con -= 1
    if con == 0:
        print(f"¡Lo siento! el número a adivinar era {numAdivinar}")
        break
    if numAdivinar > numUser:
        print("El número a adivinar es mayor \n")
        print(f"Te quedan {con} intentos")
    else:
        print("El número a adivinar es menor \n")
        print(f"Te quedan {con} intentos \n")
    numUser = int(input("Ingresa tu número: "))
else:
    print(f"\n¡Excelente lo has logrado en {11 - con} intentos!")
    print(f"\n¡Efectivamente el número era {numAdivinar}!")
