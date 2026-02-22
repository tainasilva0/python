# operadores
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:')) 

# aritméticos
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
resto = n1 % n2
expo = n1 ** n2
print(f'Soma: {soma} \nSubtração: {sub} \nMultiplicação: {multi} \nDivisão: {div} \nResto: {resto} \nExponenciação: {expo}')

print()

# relacionais
print(f'Maior: {n1 > n2}')
print(f'Menor: {n1 < n2}')
print(f'Igual: {n1 == n2}')
print(f'Maior ou igual: {n1 >= n2}')
print(f'Menor ou igual: {n1 <= n2}')
print(f'Diferente: {n1 != n2}')