# módulo de matemática > impor tmath
# funções: ceil = arredondamento pra cima
#          floor = arredondamento pra baixo
#          trunc = elemina número quebrado
#          pow = potência = **
#          sqrt = raiz quadrada
#          factorial = fatorial
# se deseja utilizar apenas uma função do módulo usar:
# fron math import sqrt

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual à {:.2f}'.format(num, raiz))
print('##################################################')
print('Número aleatório')
import random
num = random.randint(1, 100)
print(num)
