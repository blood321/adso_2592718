import mimodulo
from mimodulo import suma, resta
from mimodulo import *


# importado desde import mimodulo
print(mimodulo.suma(4, 3))
print(mimodulo.resta(10, 9))

# importado desde from mimodulo import suma y resta
print(mimodulo.suma(4, 3))
print(mimodulo.resta(10, 9))

# Importando todas las funciones del modulo mi modulo con el *
print(mimodulo.suma(4, 3))
print(mimodulo.resta(10, 9))

import sys
print(sys.path)

sys.path.append(r'D:/adso_2592718/12-modulos')

