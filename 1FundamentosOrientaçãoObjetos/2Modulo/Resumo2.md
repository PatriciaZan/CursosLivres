# Heranças
    Tipos de variaveis -> int, str, float, bool

    Classe de Origem -> SuperClasse -> Classe Mãe
    Nova Classe -> SubClasse -> Classe Filha

    Fazer  referência a uma SuperClasse.
    Uma classe filha vai herdar atributos e métodos de uma classe mãe.
    Novas classes herdam métodos e atributos da superclasse.

    Classes já prontas -> Object, Int, Float, Str, List, Tuple, Dict, Set, Bool

''1.EX.py''

## Como acessar a superclasse

''2.EX.py''

## Polimorfismo
    Mudar de forma.
    Um Objeto pode assumir várias formas, na hora da execução
    Permite que classes filhas sejam capazes de utilziar métodos já pré-estabelecidos da classe mãe, assumindo outra funcionalidade.

    -Assinatura de um método -> nome dele, primeira linha
     `def metodo(self, parametro1, parametro2, parametro3): 
        pass`
    
''3.EX.py''

## Interface
    É uma classe que será herdada por outras classes, com métodos ocos e não possui construtor.
    Uma combinação, contrato, subclasse concorda aos termos da Superclasse
    Recurso para definir ações.
    'Duck Tape' 

''4.EX.py''

## Métodos Abstratos
    Classe abstrata -> especial, não pode ser instanciada. definem os métodos e atributos que devem ser obrigatorios ao implmentar nas suas classes filhas.
    Modulo ABC 
''5.EX.py''