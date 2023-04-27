from ContasBanco import ContaCorrente
from ContasBanco import CartaoCredito

# programa
conta_lira = ContaCorrente("Lira", "111.222.333-45", 1220, 340563)

cartao_lira = CartaoCredito("Lira", conta_lira)

print(cartao_lira._numero)
print(cartao_lira._cod_seguranca)

