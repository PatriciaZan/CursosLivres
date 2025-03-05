import abc

class Minha_Interface(abc.ABC):
    @abc.abstractmethod
    def meu_metodo(self):
        pass

# OU

from abc import ABC
class Minha_Interface2(ABC):
    pass