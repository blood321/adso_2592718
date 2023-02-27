"""
Variables locales: se definen dentro de la función y no
se puedes usar fuera de ella, solo están disponibles dentro.

Variables globales: son las que se declaran fuera de una función
y están disponible dentro y fuera de ellas.
"""

# Variable Global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)

def holamundo():
    frase = "Hola Mundo!!"
    print(frase)
holamundo()

# Cuando una variable es declarada de manera global
# se puede utilizar dentro de todo el código,
# miestras que las variables declaras en el ambito de una función
# solo se pueden utilizar en ese ambito local, es decir por parte
# función o el bloque de código donde se encuentre la variable.