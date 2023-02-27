asignatura = ["Filosofía", "Matemática", "Física", "Química", "Historia", "Español"]
notas = []

for i in range(len(asignatura)):
    notas.append(input(f"ingrese una nota para {asignatura[i]}: "))
    
for i1, i2 in zip(asignatura, notas):
    print(f"En la asignatura {i1} has sacado {i2}")