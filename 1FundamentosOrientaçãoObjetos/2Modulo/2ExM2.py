class ClassePai:
    def metodo_da_super_classe(self):
        print("Método da SuperClasse")

class ClasseFilho(ClassePai):
    def metodo_da_subclasse(self):
        super().metodo_da_super_classe()
        print("Método da SubClasse")

objeto = ClasseFilho()
object.metodo_da_subclasse()

# Segundo Exemplo

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return (f"""
                    Funcionario: {self.nome}
                    Salário: {salf.salario}""")
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def __str__(self):
        return f"""
        Gerente: {self.nome}
        Salário; {self.salario}
        Bônus: {self.bonus}"""
    
funcionario = Funcionario("Maria", 2700)
print(funcionario)

gerente = Gerente("Carla", 5500, 1500)
print(gerente)

# Exercicio #################

# Criar uma SuperClasse chamada Veiculo com atributos marca, modelo
# Crie os métodos acelerar , frear
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def acelerar(self):
        print(f"""Acelerando {self.marca}""")

    def frear(self):
        print(f"""Freando {self.marca}""")

# Crie duas subclasses: Carro e moto que herdam da classe Veiculo
# Implemente metodos especificos
class Carro(Veiculo):
    def acionar_alarme(self):
        print(f"O {self.modelo} {self.marca} com o alarme ativado!")


class Moto(Veiculo):
    def acionar_luz(self):
        print(f"O {self.modelo} {self.marca} está com a luz acessa!")