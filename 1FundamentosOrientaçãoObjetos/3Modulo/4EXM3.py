from abc import ABC, abstractmethod

class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Alimentacao(ABC):
    @abstractmethod
    def comer(self):
        pass

class Descanco(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Robo(Trabalhador):
    def trabalhar(self):
        print("O robô está trabalhando")

class Humano(Trabalhador, Alimentacao, Descanco):
    def trabalhar(self):
        print("O humano está trabalhando")
    def comer(self):
        print("O humano está comendo")
    def dormir(self):
        print("O humano está dormindo")

humano = Humano()
humano.trabalhar()
humano.comer()
humano.dormir()

robo = Robo()
robo.trabalhar()