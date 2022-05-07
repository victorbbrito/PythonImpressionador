# Set

# estrutura: meu_set = {valor,valor,valor,valor,valor}
# não pode ter valores duplicados
# não tem ordem fixa

set_produtos = {'arroz', 'feijao', 'azeite', 'atum'}

print(set_produtos)

cpf_clientes = ['762.354.548-89', '451.246.330-77', '445.213.304-85', '762.354.448-89',
                '451.246.330-77', '495.213.304-85', '762.354.548-89', '431.246.330-87', '445.213.364-95']

set_cpf_clientes = set(cpf_clientes)
cpf_unicos = list(set_cpf_clientes)
print('Quantidade de clientes: {}'.format(len(cpf_clientes)))
print('Quantidade de clientes unicos: {}'.format(len(cpf_unicos)))
