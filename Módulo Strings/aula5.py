# principais formatações usando .format()
# :< alinhar o texto a esquerda (se houver espaço na tela para isso)
# :> alinhar o texto a direita (se houver espaço na tela para isso)
# :^ alinha o texto ao centro (se houver espaço na tela para isso)
# :+ coloca o sinal sempre a frente do número (independente se for negativo ou positivo)
# :, coloca a virgula como separador de milhar
# :_ coloca o _ como separador de milhar
# :e formatao científico
# :f número com quantidade fixa de casas decimais
# :x formato HEX minusculo (para cores)
# :X formato HEX maiúculo (para cores)
# :% formato percentual

print('O indice é {}'.format(1000))

e_mail = 'vlbb@icomp.ufam.edu.br'

# o 30 limita o tamanho do indice que irá aparecer
print('Meu email não é {:>30}'.format(e_mail))

custo = 500
faturamento = 270
lucro = faturamento - custo
# formatação para exibir o sinal negativo e positivo

print('Faturamento foi de :{:+} e o lucro foi de {:+}'.format(faturamento, lucro))

custo = 5000
faturamento = 2700
lucro = faturamento - custo

# exemplo de formatação usando o semparador de milhar como (,)
print('Faturamento foi de :{:,} e o lucro foi de {:,}'.format(faturamento, lucro))

# exemplo de formatação usando o semparador de milhar como (,) e formatação para exibir o sinal negativo e positivo
print('Faturamento foi de :{:+,} e o lucro foi de {:+,}'.format(faturamento, lucro))

# exemplo de formatação para limitar as casas decimais
print('Faturamento foi de :{:.2f} e o lucro foi de {:.2f}'.format(faturamento, lucro))

# exemplo de formatação para percentual
margem = lucro / faturamento
print('A margem de faturamento foi de :{:.2%}'.format(margem))

# exemplo de formatação para moeda
print('Faturamento foi R${:,.2f} e o lucro foi R${:,.2f}'.format(faturamento, lucro))

imposto = 0.15758
preco = 100
valor_imposto = round( preco * imposto, 1) # arredondar um número
print('Imposto sobre o preço é de {}'.format(valor_imposto))

