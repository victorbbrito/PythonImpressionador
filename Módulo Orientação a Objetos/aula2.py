# class nome_da_classe:
#
# Dentro da classe, vamos criar a "função" método __init__
# Esse método é quem define o que acontece quando você cria uma instancia dessa classe
#
#

class TV:
    
    def __init__(self):
        self.cor = None
        self.ligada = False
        self.tamanho = None
        self.canal = None
        self.volume = None
    
    def setCor(self, cor:str):
        self.cor = cor.capitalize()
        return self        
    
    def setLigada(self, status:bool):
        self.ligada = status
        return self
    
    def setTamanho(self, tamanho:int):
        self.tamanho = tamanho
        return self
        
    

tv_sala = TV()

print(tv_sala.cor)
tv_sala.setCor('preto')

print(tv_sala.cor)
