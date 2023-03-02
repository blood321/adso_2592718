import matematicas.aritmetica

print(matematicas.aritmetica.sumar(7, 5))


from matematicas.aritmetica import sumar

print(sumar(7, 5))

from matematicas.aritmetica import sumar, restar, mult, div
from matematicas.aritmetica import *

print(sumar(10, 50))
print(restar(10, 50))
print(mult(10, 50))
print(div(10, 50))