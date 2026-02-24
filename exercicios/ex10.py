# quantidade de tinta
largura = float(input('Digite a largura da parede (em m):'))
altura = float(input('Digite a altura da parede (em m):'))

area = largura * altura
print(f'Sua parede tem {area} metros quadrados.')

tinta = area / 2
print(f'Serão necessários {tinta} litros de tinta para pintar a parede.')