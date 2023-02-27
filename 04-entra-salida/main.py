# Entrada
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad?")

# Salida de datos con metodo Format
print(f"Me alegro de conocerte, bienvenido {nombre}, veo que tienes {edad} años!!")

# Saluda de datos parseando la variable edad para cambiar el valor a un entero y sumarle 2
print(f"Me alegro de conocerte, bienvenido {nombre}, veo que tienes {int(edad) + 2} años!!")
