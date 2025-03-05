
class Pessoa:
    def __init__(self,nome):
        self.nome = nome
class Amigo(Pessoa):
    pass

juca = Amigo("João")
print(f"Meu Amigo {juca.nome}.")

# Segundo Exemplo

class Pessoa2:
    def __init__(self, nome, altura, cor_cabelo):
        self.nome = nome
        self.altura = altura
        self.cor_cabelo = cor_cabelo

    def pinter_cabelo(self, nova_cor):
        self.cor_cabelo = nova_cor

class Amigo2(Pessoa2):
    def __init__(self,apelido, nome, altura, cor_cabelo):
        super().__init__(nome, altura, cor_cabelo)
        self.apelido = apelido

    def mostrat_dados(self):
        print(f"Nome: {self.nome} - {self.apelido}")
        print(f"Altura: {self.altura}")
        print(f"Cor Cabelo; {self.cor_cabelo}")

amigoA = Amigo2("DnaAna", "Ana", 170, "Branca")
amigoA.pinter_cabelo("Azul")
amigoA.mostrat_dados()