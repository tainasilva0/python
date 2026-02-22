# conversor de medidas
medida = int(input('Digite a medida do seu cômodo (em m):'))

decimetro = medida * 10
centimetro = medida * (10 ** 2)
milimetro = medida * (10 ** 3)
decametro = medida / 10
hectometro = medida / (10 ** 2)
quilometro = medida / (10 ** 3)

print(f'Convertendo pra dm: {decimetro}')
print(f'Convertendo pra cm: {centimetro}')
print(f'Convertendo pra mm: {milimetro}')
print(f'Convertendo pra dam: {decametro}')
print(f'Convertendo pra hm: {hectometro}')
print(f'Convertendo pra km: {quilometro}')