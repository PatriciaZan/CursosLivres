class Cadastro:
    def cadastrar(sel, name, idade):
        #if isinstance(nome, str) and isinstance(idade, int):
        if self.__verificar_dados(self, nome, idade):
                self.__armazenar_dados(nome,idade)
        else:
            self.__retornar_erro()

    def __verificar_dados(self,nome,idade):
        if isinstance(nome, str) and isinstance(idade,int):
                return True
        return False
    
    def __armazenar_dados(self,nome,idade):
        # Acessando BD...
        # Cadastrando o usuário...
        pass

    def __retornar_erro(self):
        #OPS. Dados inválidos
        pass