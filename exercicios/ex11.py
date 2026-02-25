# desconto
produto = float(input('Digite o valor do seu produto: R$'))
cupom = float(input('Aplique o cupom de desconto (se houver):'))

desc = produto * (cupom / 100)

print(f'O seu produto de R${produto} custa R${desc} com o cupom aplicado.')