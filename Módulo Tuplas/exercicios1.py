meta = 10000
vendas = [
    ('João',15000),
    ('Julia', 27000),
    ('Marcos', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alan', 7870)
]

for vendendor, quantidade in vendas:
    if quantidade >= meta:
        print('{} bateu a meta, vendeu {}.'.format(vendendor, quantidade))

