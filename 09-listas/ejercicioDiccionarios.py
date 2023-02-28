import sys

f = {
    "Platano": 2000,
    "Manzana": 1200,
    "Pera": 1000,
    "Naranja": 500
    }

for x in f:
    print("frutas disponibles", x)

fruta = input("Elige una fruta: ").capitalize()

for i in f:
    if i != fruta:
        fruta = i
    else:
        print("La fruta no existe en la lista")
        sys.exit()
    
kilo = int(input(f"Cuantos kilos de {fruta} quieres: "))

for j in f:
    if j == fruta:
        valFruta = f[j]
        valor = valFruta * kilo

print(f"El valor de {kilo} kilo(s) de {fruta} es: {valor}")
