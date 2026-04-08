from random import randint
from time import sleep

print('-=' * 22)
print('Bora jogar?')
print('Vou pensar em um número entre 0 e 10.')
print('-=' * 22)

num = int(input(('Descubra qual número escolhi: ')))
computador = randint(0,10)

print('Pensando...')
sleep(2)

if num == computador:
    print('Acertou!')
else:
    print('Errou!')