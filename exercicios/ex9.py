# conversor de moedas
dinheiro = float(input('Quanto você tem disponível? R$'))
dolar = dinheiro / 5.15
euro = dinheiro / 6.09
iene = dinheiro / 0.033
peso = dinheiro / 0.037

print(f'Essa quantia em reais corresponde a {dolar} dólares.')
print(f'Essa quantia em reais corresponde a {euro} euros.')
print(f'Essa quantia em reais corresponde a {iene} ienes.')
print(f'Essa quantia em reais corresponde a {peso} pesos.')