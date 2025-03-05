class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Cachorro late!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Gato mia!"
    
    def animal_atitude(animal: Animal):
        print(animal.emitir_som())

cachorro = Cachorro()
gato = Gato()

animal_atitude(cachorro)
animal_atitude(gato)