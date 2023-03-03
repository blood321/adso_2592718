from clasesPadres import Padre

# class Hija:
#     def __init__(self, ojos, cejas, caras) -> None:
#         Padre.__init__(self, ojos, cejas)
#         self.caras = caras

# tomas = Hija('Marrones', 'Negras', 'Largas')
# print(tomas.ojos, tomas.cejas, tomas.caras)

class Hija(Padre):
    def __init__(self, ojos, cejas, caras) -> None:
        super().__init__(ojos, cejas)
        self.caras = caras

tomas = Hija('Marrones', 'Negras', 'Largas')
print(tomas.ojos, tomas.cejas, tomas.caras)