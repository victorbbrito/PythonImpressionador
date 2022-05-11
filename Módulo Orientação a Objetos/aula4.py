import time

from matplotlib.pyplot import switch_backend

segundos_hoje = time.time()
print(segundos_hoje)

segundos_hoje = time.ctime()
print(segundos_hoje)

tempo_inicial = time.time()
for i in range(1000000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print(duracao)

print('Começando')
time.sleep(5)
print('Rodou 5 segundos após')

data_atual = time.gmtime()
print(data_atual)

ano = data_atual.tm_year
mes = data_atual.tm_mon
dia = data_atual.tm_mday
hora = data_atual.tm_hour
dia_semana = data_atual.tm_wday

print('Hoje é dia {}/{}/{}'.format(dia, mes, ano))
