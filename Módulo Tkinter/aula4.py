import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e-mails promocionais ?", variable= var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text="Aceitar temos de uso e politicas de privacidade", variable=var_politicas)
checkbox_politicas.grid(row=1, column=0)

def enviar():
    if var_promocoes.get():
        print("O usuário deseja receber promoções.")
    else:
        print("O usuário NÃO deseja receber promoções.")
    if var_politicas.get():
        print("O usuário aceita os termos de uso.")
    else:
        print("O usuário NÃO aceita os termos de uso.")

botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=2, column=0)

janela.mainloop()