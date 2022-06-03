# O que queremos saber ?

'''
    1. Valor total da folha salarial -> Qual foi o 
    gasto total com salários de funcionários pela empresa ?

    2. Qual foi o faturamento da empresa ?

    3. Qual a % de funcionários que já fechou algum contrato?

    4. Calcule o total de contratos que cada área da empresa fechou.

    5. Calcule o total de funcionários por área

    6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?

'''

import pandas as pd

# caminhos dos documentos da base de dados
funcionarios_csv = r'PythonImpressionador\Módulo Pandas\Projeto Análise de Dados\CadastroFuncionarios.csv'
clientes_csv = r'PythonImpressionador\Módulo Pandas\Projeto Análise de Dados\CadastroClientes.csv'
servicos_xlsx = r'PythonImpressionador\Módulo Pandas\Projeto Análise de Dados\BaseServiçosPrestados.xlsx'

# importar os dados para os dataframes
funcionarios_df = pd.read_csv(funcionarios_csv, sep=';', decimal=',')
clientes_df = pd.read_csv(clientes_csv, sep=';')
servicos_df = pd.read_excel(servicos_xlsx)

# tratamento da base de dados

# retirar colunas estado civil e cargo da tabela de funcinários
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)

# 1 ->
funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + \
    funcionarios_df['Impostos'] + funcionarios_df['Beneficios']
print('Total da folha slarial mensal é de R${:,}'.format(
    funcionarios_df['Salario Total'].sum()))

# 2 ->
faturamentos_df = servicos_df[['ID Cliente', "Tempo Total de Contrato (Meses)"]].merge(
    clientes_df[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamentos_df['Faturamento Total'] = faturamentos_df[
    'Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']
print('Faturamento Total: R${:,}'.format(
    sum(faturamentos_df['Faturamento Total'])))

# 3 ->
qntd_funcionarios = len(funcionarios_df['ID Funcionário'])
qntd_funcionarios_fecharam_contrato = len(
    servicos_df['ID Funcionário'].unique())
print('Percentual Funcionários Fecharam contrato: {:.2%}'.format(
    qntd_funcionarios_fecharam_contrato/qntd_funcionarios))

# 4 ->
contratos_area_df = servicos_df[['ID Funcionário']].merge(
    funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')
contratos_area_quantidade = contratos_area_df['Area'].value_counts()
print(contratos_area_quantidade)

# 5 ->
funcionarios_por_area = funcionarios_df['Area'].value_counts()
print(funcionarios_por_area)

# 6 ->
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('Ticket Médio Mensal: R$ {:,.2f}'.format(ticket_medio))
