# c0 = int(input("Ingresa tu numero: "))
# paso = 0
# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 //= 2
#     else:
#         c0 *= 3
#         c0 += 1
#     paso += 1
#     print(c0)
# print(f"Pasos = {paso}")

#---------------------------------------------------------------#

# n = 3

# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

#-----------------------------------------------------------------#
# operario = 5
# totNomina = 0
# salario = 30000

# while operario > 0:
#     horaOpera = int(input("ingrese el número de horas: "))
#     totNomina += salario * horaOpera
#     operario -= 1

# print(f"La nómina total de los trabajadores es {totNomina}")

# email = input("ingresa tu email: ")

# for letter in email:
#     if letter == "@":
#         print("El correo es correcto")
# print("el correo no es valido")

#-------------------------------------------------------------------------#

# Creo una función que sume dos parametros
def suma(a, b):
    return a + b

# Solicito al usuario que ingrese un número y creo dos variables inicializadas en 0,
# en un ciclo while sumo los números y muestro por pantalla el resultado,
# realizando la suma de los valores que entran y acumulando la suma para que al final muestre la suma total de los valores ingresados.
num1 = int(input("ingresa un número: "))
num2 = 0
sumaTotal = 0
while num1 != 0:
    sumaNum = suma(num1, num2)
    print(f"La suma de tus números es: {sumaNum}")
    num2 = num1
    sumaTotal += num1
    num1 = int(input("ingresa un número: "))
else:
    print(f"La suma de tus números es: {sumaNum}")
    print(f"La suma total de los números digitados es: {sumaTotal}")



