asignatura = ["Filosofía", "Matemática", "Física", "Química", "Historia", "Español"]
notasEs = []

for i in notasEs:
    notasEs.append(i + 1)

for i1, i2 in zip(asignatura, notasEs):
    print(i1, i2)
    print(f"En la asignatura {i1} has sacado {i2}")