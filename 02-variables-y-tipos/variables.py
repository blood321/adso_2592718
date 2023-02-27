"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto 

"""
# Cerrar variables y asignarles un valor
texto = "SENA Formación Python"
texto2 = "Andrés Guzmán"
numero = "36"
decimal = "7.6"

# Mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("----------------------------------------------------")

# Sustituir el valor de algunas variables / reasignando valores
numero = "20"
decimal = "13.2"
print(numero)
print(decimal)

#Concatenación
nivel = "TECNOLOGO"
nombre = "ADSO"
centro = "Agropecuario"

print(nivel + " " + nombre + " - " + centro)
print("----------------------------------------------------")
print(f"{nivel} {nombre} - {centro}")
print("Hola soy {} {} y mi centro de formación es: {}".format(nivel, nombre, centro))
