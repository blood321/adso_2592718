nombre = "ADSO SENA Agrotics"

#Funciones Generales

print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un String")
else:
    print("Esa Variable NO es una String")
if not isinstance(nombre, float):
    print("Esa variable NO es un número con decimales")

# Limpiar espacios de un String
frase = "       mi contenido        "
print(frase)
print(frase.strip())

#Eliminar variable
year = 2022
del year

# Comprobar Variable vacia
texto = " fff "
if len(texto) <= 0:
    print("La variable está vacia")
else:
    print("La variable tiene contenido:", len(texto))

# Encontrar caracteres en un texto
frase = "La vida es bella"
print(frase.find("vida"))

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#Mayusculas y minusculas
print(frase)
print(frase.lower())
print(frase.upper())

