class Camisa:
    def vestir(self, camisa):
        camisa.vestir()

class Lisa:
    def vestir(self):
        print("Vesti a camisa lisa!")

class Xadrez:
    def vestir(self):
        print("Vesti a camisa xadrez!")

camisa = Camisa()

lisa = Lisa()
xadrez = Xadrez()

camisa.vestir(lisa)