from carro import Carro

carro = Carro("Azul", "Renault", "Clio", 150, 200, 4)
carro1 = Carro("Amarillo", "Chevrolt", "Corsa", 250, 200, 4)
carro2 = Carro("Rojo", "Citroen", "Xara", 350, 200, 4)
carro3 = Carro("Negro", "Volkwagen", "Virtus", 430, 200, 4)
# print(carro.getColor())
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar Tipado
# carro3 = "Aleatorio"
if type(carro3) == Carro:
    print("Es un objeto correcto")
else:
    print("No es un objeto!!")

# Visibilidad
print(carro.soy_publico)
print(carro.__soy_privado)