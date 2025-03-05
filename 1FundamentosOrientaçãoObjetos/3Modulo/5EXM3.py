from abc import ABC, abstractmethod

class InterruptorInterface(ABC):
    @abstractmethod
    def Ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Lampada(InterruptorInterface):
    def ligar(self):
        print("Ligada")
    
    def desligar(self):
        print("Desligada")

class Quarto:
    def __init__(self, interruptor: Interruptor):
        self.interruptor = interruptor
    def acender_luz(self):
        self.interruptor.ligar()
    def apagar_luz(self):
        self.interruptor.desligar()

quarto = Quarto(Lampada())
quarto.acender_luz()
quarto.apagar_luz()