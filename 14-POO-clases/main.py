# Programación Orientada a Objetos (POO o OOP)
# Definir una clase(molde para crear  más objetos de ese tipo)
# en nuestro caso (carro) con caracteristicas similares)

class Carro:
    # Atributos o propiedades (variables)
    # Caracteristicas del Carro
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # metodos, son acciones que hacen los objetos(coche)(funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
# Fin definición de clase

#Crear objeto / Intanciar la Clase



carro = Carro()
# print(carro.marca, carro.color)
# print("Velocidad Actual: ", carro.velocidad)
# carro.acelerar()
# carro.acelerar()
# carro.acelerar()
# carro.acelerar()
# carro.frenar()
# print("Velocidad nueva: ", carro.velocidad)


# carro = Carro()
# print(carro.marca, carro.color)
# print("Velocidad Actual: ", carro.velocidad)
# carro.acelerar()
# carro.acelerar()
# carro.acelerar()
# carro.acelerar()
# carro.frenar()
# print("Velocidad nueva: ", carro.getVelocidad())


# carro = Carro()
# carro.setColor("amarillo")
# carro.setModelo("Murcielago")
# print(carro.marca, carro.getModelo(), carro.getColor())
# print("Velocidad Actual: ", carro.velocidad)
# carro.acelerar()
# carro.acelerar()
# carro.acelerar()
# carro.acelerar()
# carro.frenar()
# print("Velocidad nueva: ", carro.velocidad)

print("CARRO 1:")
carro.setColor("amarillo")
carro.setModelo("Murcielago")
print(carro.marca, carro.getModelo(), carro.getColor())
print("Velocidad Actual: ", carro.velocidad)
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.frenar()
print("Velocidad nueva: ", carro.velocidad)

print("------------------------------------------------")
print("CARRO 2")

# Crear más objetivo
carro2 = Carro()
carro2.setColor("Verde")
carro2.setModelo("Gallardo")
print(carro2.marca, carro2.getModelo(), carro2.getColor())