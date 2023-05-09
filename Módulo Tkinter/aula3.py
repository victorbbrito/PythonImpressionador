import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Cotação de Moedas")

# ajusta a linha 1
janela.rowconfigure(0, weight= 1)
# ajustar a coluna 0 1 para auto ajustar
janela.columnconfigure([0,1], weight=1) 

mensagem = tk.Label(text = "Sistema de Busca de Cotação de Moedas", background = 'black', foreground = '#fff', width = 35, height = 5)
mensagem.grid(row=0, column=0, columnspan=3, sticky="NSEW")

# N - north 

mensagem2 = tk.Label(text = "Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

#moeda = tk.Entry()
#moeda.grid(row=1, column=1, sticky="NSEW")

dicionario_cotacoes = {
    'Dólar': 5.00,
    'Euro': 5.47,
    'Libra': 6.30,
    'Bitcoin': 137325.20,
    'Ethereum': 9208.14,
}

moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

def buscar_cotacao():
    moeda_entry = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_entry)
    
    mensagem_cotacao = tk.Label(text="Cotação não encontrada")
    mensagem_cotacao.grid(row=3, column=0, columnspan=3, sticky= "NSEW" )
    
    if cotacao_moeda:
        # exibir a cotacao da moeda
        
        mensagem_cotacao["text"] = "Cotação do {} é de R${:,.2f} .".format(moeda_entry, cotacao_moeda)
    else:
        mensagem_cotacao
    
botao = tk.Button(text="Buscar", command= buscar_cotacao)
botao.grid(row=1, column=2, sticky= "NSEW")

mensagem3 = tk.Label(text='Caso queira pegar mais de uma cotação ao mesmo tempo, digite uma moeda em cada linha.')
mensagem3.grid(row=4, column=0, columnspan= 2)

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky= "NSEW")

def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista = texto.split('\n')
    mensagem_cotacoes = []
    for item in lista:
        cotacao= dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append("{}: {:,.2f}".format(item, cotacao))
    mensagem4 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=0, columnspan= 2)

botao_mutiplas = tk.Button(text="Buscar Cotações", command= buscar_cotacoes)
botao_mutiplas.grid(row=5, column=1)


janela.mainloop()
