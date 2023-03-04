pares = []
impares = []

# def solNum():
n = int(input("Ingresa el valor para la longitud de la lista: "))
if n <= 20 and n >= 1:
    while len(pares) != n or len(impares) != n:
        num = int(input("Ingresa un número entero: "))
        if num % 2 == 0:
            if len(pares) == n:
                print("El vector de los pares está lleno")
                continue
            else:
                pares.append(num)
                pares.sort()
        elif num % 2 != 0:
            if len(impares) == n:
                print("El vector de los impares está lleno")
                continue
            else:
                impares.append(num)
                impares.sort()
    else:
        print("Los vectores están llenos")
    print("Vector de pares", pares)
    print("Vector de impares", impares)
else:
    print("Debe ingresa un valor entre 1 y 20")