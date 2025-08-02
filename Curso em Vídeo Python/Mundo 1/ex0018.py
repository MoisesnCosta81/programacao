
#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#  do seno, cosseno e tangente desse ânglo.
# todo valor de seno, cosseno deve ser convertido em radiano.

import math
ângulo = float(input('Qual é o ângulo? '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(ângulo, tangente))
print('-'*60)
