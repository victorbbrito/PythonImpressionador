from datetime import datetime
import pytz
from random import randint

class ContaCorrente():
    
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Attributos:
        nome (str): Nome do Cliente
        cpf (str): Numero de CPF do Cliente
        agencia (int): Agencia responsavel pela conta do cliente
        num_conta: Numero da conta corrente do cliente
        limite: Limite de Cheque especial do cliente
        transacoes: Historico de transacoes do cliente
    """
    
    @staticmethod
    def _dataHora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y - %H:%M:%S')
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo:float = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []
    
    def consultarSaldo(self):
        """
            Exibe o saldo atual da conta do cliente.
            Não há parametros necessários.
        """
        msg = "Seu saldo atual é de R$ {:,.2f}".format(self._saldo)
        print(msg)
        
    def depositar(self, valor:float):
        """
            Depositar valor na conta do usuário.
            Attributes:
            valor (float): valor a ser depositado na conta.
        """
        
        self._saldo += valor
        self._transacoes.append(("DEPOSITO",valor, self._saldo, self._dataHora()))
        self.consultarSaldo()
    
    def _limiteConta(self):
        self._limite = -(self._saldo*0.20)
        return self._limite
    
    def sacar(self, valor:float):
        """
            Sacar valor na conta do usuário.
            Attributes:
            valor (float): valor a ser sacado na conta.
        """
        
        if (self._saldo - valor) < self._limiteConta() :
            print("Valor de saque é maior que o seu limite disponível") 
            self.consultarSaldo
            pass
        else:
            self._saldo -= valor
            self._transacoes.append(("SAQUE",-valor, self._saldo, self._dataHora()))
    
    def consultarLimiteChequeEspecial(self):
        """
            Exibe o limite do cheque especial da conta do cliente.
            Não há parametros necessários.
        """
        
        print("Seu limite de cheque especial é de R${:,.2f}".format(self._limiteConta()))
        
    def consultarHistoricoTransacoes(self):
        """
            Exibe o historico de transações da conta do cliente.
            Não há parametros necessários.
        """
        
        print("Hisórico de Transações")
        for transacao in self._transacoes:
            print(transacao)
            
    def transferir(self, valor:float, conta_destino):
        """
            Transfere o valor de uma conta para outra conta.
            Retira de uma conta o valor e adiciona em outra conta.
            Attributes:
            valor (float): valor a ser transferido
            conta_destino (ContaCorrente): conta corrente de destino
        """
        
        self._saldo -= valor
        self._transacoes.append(("TRANSFERENCIA ENVIADA",-valor, self._saldo, self._dataHora()))
        conta_destino._saldo += valor
        conta_destino.transacoes.append(("TRANSFERENCIA RECEBIDA",valor, conta_destino._saldo, conta_destino._dataHora()))
        
        
class CartaoCredito:
    
    @staticmethod
    def _data():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self._numero = randint(1000000000000000, 9999999999999999)
        self._titular = titular
        self._validade = "{}/{}".format(self._data().month, self._data().year + 3)
        self._cod_seguranca = "{}{}{}".format(randint(0,9),randint(0,9),randint(0,9))
        self._limite = 1000
        self._senha = None
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
      
    @property  
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida")
        

