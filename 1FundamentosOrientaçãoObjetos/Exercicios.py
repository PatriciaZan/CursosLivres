# EXERCICIO ABAJUR
# Possui penas um botão, quando tocado:
# 1 vez -> acende a lâmpada na intensidade fraca
# 2 vez -> acende a lâmpada na intensidade média
# 3 vez -> acende a lâmpada na intensidade forte
# 4 vez -> apaga a lâmpada

class Abajur:
    def __init__(self):
        self.__lampada = False # False - apagada True - acesa
        self.__intensidade = 0 # 0, 1, 2, 3 
    def __liga_desliga_lampada(self):
        if self.__intensidade == 0:
            self.__lampada = False
        else:
            self.__lampada = True

    def __controla_intensidade(self):
        self.__intensidade += 1
        if self.__intensidade == 4:
            self.__intensidade = 0

    def tocar_botao(self):
        if input("Tocar [Enter]") == "":
            return True
        return False
            
    def mostrar_status(self):
        print("Status")
        print(" -", self.__lampada)
        print(" -", self.__intensidade)

    def acoes(self):
        self.__controla_intensidade()
        self.__liga_desliga_lampada()

abajur = Abajur()

while True:
    if abajur.tocar_botao():
        abajur.acoes()
    abajur.mostrar_status() # Status: -True -1