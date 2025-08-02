# Criar programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua porção inteira.

import math

# truncate elimina os números depois da vírgula
num = float(input('Digite um número real: '))
inteiro = math.trunc(num)
print('O número digitado foi {} e seu número interio é: {}'. format(num, inteiro))
# Alinhando strings :
# print(f"|{'-':^40}")
print('-'*40)

#menor linha

from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e o seu número real é: {}'.format(num, trunc(num)))

print('-'*40)
