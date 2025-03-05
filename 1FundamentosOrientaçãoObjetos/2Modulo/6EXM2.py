class MinhaClasse:
    @staticmethod
    def meu_metodo_estatico():
        print("Este método é estático!")

# Como acessar este método?
MinhaClasse.meu_metodo_estatico()

# Exemplo
import math

class Calcuadora:
    @staticmethod
    def raiz_quadrada(n):
        return math.sqrt(n)
    
print(Calcuadora.raiz_quadrada(16))