# cálculo de média e resultado

aluno = input('Qual seu nome?')
print(f'Seja bem-vindo ao sistema de notas, {aluno}!')
print()

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = (nota1 + nota2) / 2
res = print(f'Sua média é {media}.')

if(media >= 6):
    print(f'{aluno}, você está APROVADO.')
else:
    print(f'{aluno}, você está REPROVADO.')