# Análise textual
frase = str(input('Digite uma frase: ')).strip().upper()

print('Número de caracteres:', len(frase))

print('Transformar tudo em maiúsculo: {}'.format(frase.upper()))
print('Transformar tudo em minúsculo: {}'.format(frase.lower()))

print('Essa frase em lista: {}'.format(frase.split()))

print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A última letra "A" aparece na {} posição'.format(frase.rfind('A')+1))