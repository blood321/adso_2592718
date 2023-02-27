"""

FOR, estructura iteractiva que se repite
for variable en elemento_iterable (lista, rango, etc)
    Bloque de intrucciones
"""

print("\n######### EJEMPLO 1 ###########")

# contador = 0
# resultado = 0

# for contador in range(0, 10):
#     print("voy por el "+ str(contador))
#     resultado += contador

# print(f"el resultado es: {resultado}")

print("\n############## EJEMPLO 2 #############")

# numero_usuario = int(input("¿De que número quieres la tabla?: "))

# if numero_usuario <= 1:
#     numero_usuario = 1

# print(f" ### Tabla de multiplicar del número {numero_usuario} ###")

# for numero_tabla in range(0, 10):
#     print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
# else:
#     print(f"La tabla del {numero_usuario} ha finalización")

print("\n########### EJEMPLO 3 ###########")

numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario <= 1:
    numero_usuario = 1

print(f" ### Tabla de multiplicar del número {numero_usuario} ###")

for numero_tabla in range(0, 10):
    if numero_usuario >= 10:
        print("Solo se admiten numero del 1 al 9")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print(f"La tabla del {numero_usuario} ha finalización")

