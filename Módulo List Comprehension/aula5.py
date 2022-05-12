
produtos = ['coca','pepsi','guarana','skol','brahma','agua','del valle','dolly','red bull']
vendas = [1200,300,800,1500,1900,2750,400,20,23]
top5 = ['agua','brahma','skol','coca','del vale']

# fazendo com for
total_top5 = 0
for i, produto in enumerate(produtos):
    if produto in top5:
        total_top5 += vendas[i]

print(total_top5)

print('Top 5 representou {:0.1%} das vendas'.format(total_top5/sum(vendas)))

# fazendo com list comprehension

total_top5 = sum(vendas[i] for i, produto in enumerate(produtos) if produto in top5)
print(total_top5)

print('Top 5 representou {:0.1%} das vendas'.format(total_top5/sum(vendas)))
