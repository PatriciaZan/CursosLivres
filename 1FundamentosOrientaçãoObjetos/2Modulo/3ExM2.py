class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro está latindo!"
    
class Gato(Animal):
    def emitir_som(self):
        return "O gato está miando!"

lista_animais = [Cachorro(), Gato()]

for animal in lista_animais:
    print(animal.emitir_som())