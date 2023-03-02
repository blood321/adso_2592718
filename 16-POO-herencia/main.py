import clases # Se importa toda la clase para tener acceso a todo el archivo

persona = clases.Persona() # Se crea un objeto persona
# Asignación  de Valores
persona.setNombre("Andrés")
persona.setApellidos("Guzmán Quinayas")
persona.setAltura("170 cm")
persona.setEdad("36 Años")

# Mostrar diferentes propiedades
print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar()) # Se accede a metodos en concreto

print("-------------------***********---------------------")

# Creación del objeto informático
informatico = clases.informartico() # Accede a las clase informático
informatico.setNombre("Julián Andrés") # Se asignan nuevos valores la objeto informático
informatico.setApellidos("Pérez Martinez")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(persona.hablar()) # Herencia
print("----------------*********---------------")