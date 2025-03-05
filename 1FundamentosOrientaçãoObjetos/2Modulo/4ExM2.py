class FiguraGenerica:
    def calcular_area(self):
        pass

class Retangulo(FiguraGenerica):
    def __init__(self, altura, largura):
       self.altura = altura
       self.largura = largura
    def calcular_area(self):
        return f"Área do Retângulo: {self.altura * self.largura}"
    
retangulo = Retangulo(10,20)
print(calcular_area(retangulo))