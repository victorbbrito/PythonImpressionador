from random import randint


class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
    
    def verificar_caixa(self):
        if self.caixa < 1000000 :
            print("Caixa a baixo do nível recomendado. Caixa atual: R${:,.2f}".format(self.caixa))
        else:
            print("O valor de caixa está ok. Caixa atual: R${:,.2f}".format(self.caixa))
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Emprestimo não é possivel. Dinheiro não disponivel em caixa.")
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome,cpf,patrimonio))
        
    
class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj, numero):
        super().__init__(telefone, cnpj, numero)
        self.site = "www.agenciavirtual.com.bt/{}".format(self.numero)
        self.caixa = 1000000
        self.caixa_paypal = 0
    
    def depositar_paypal(self, valor):
        if valor > self.caixa:
            print("Valor não disponivel em caixa")
        else:
            self.caixa -= valor
            self.caixa_paypal += valor
       
    def sacar_paypal(self, valor):
        if valor > self.caixa_paypal:
            print("Valor não disponivel no paypal")
        else:
            self.caixa_paypal -= valor
            self.caixa += valor

class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001,9999))
        self.caixa = 1000000
                

class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001,9999))
        self.caixa = 10000000
        


    