# Herencia: es la posibilidad de compartir atributos y metodos
# entre clases. Y que diferentes clases hereden de otras
class Persona: # Definimos la clase Padre
    # Metodos Getters y Setters
    # Con los get se obtienen la propiedades cuando se cree el objeto
    def getNombre(self): # Obtener el nombre
        return self.nombre
    
    def getApellidos(self): # Obtener los apellidos
        return self.apellidos
    
    def getAltura(self): # Obtener los altura
        return self.altura
    
    def getEdad(self): # Obtener la edad
        return self.edad
    # Con los set se asignan los diferentes propiedades del objeto
    def setNombre(self, nombre): # Obtener la edad
        self.nombre = nombre

    def setApellidos(self, apellidos): # Obtener la edad
        self.apellidos = apellidos

    def setAltura(self, altura): # Obtener la edad
        self.altura = altura

    def setEdad(self, edad): # Obtener la edad
        self.edad = edad

    def hablar(self): # Obtener la edad
        return "Estoy Hablando"
    
# ********** HERENCIA ***********
class informatico(Persona):
    """
    Lenguaje
    experiencia"""
    # Creamos un constructor
    def __init__(self) -> None: # Propiedades por defecto
        self.lenguajes = "HTML, CSS, Jvascript, PHP"
        self.experiencia = 5

    def getLenguajes(self): # Get
        return self.lenguajes

    def aprender(self, lenguajes): # Set
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy Programando!!"
    
    def repararPC(self):
        return "He reparado el PC"
    
class TecnicoRedes(informatico):
    def __init__(self) -> None:
        super().__init__() # Función Super para traer el constructor
        self.auditarRedes = "Experto"
        self.experiencia = 10

    def auditar(self):
        return "Estoy auditando una Red"