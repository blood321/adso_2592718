import sys
print(sys.path)
print(dir())
print("Probando paquetes: ")

from mipaquete import pruebas
from mipaquete import herramientas

pruebas.probando()
herramientas.nombreCompleto("Carlos", "Gómez")