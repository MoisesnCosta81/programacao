print('''Crie um programa que leia um número inteiro
e mostre na tela se o número é PAR ou IMPAR.''')

número = int(input('Digite um número: '))
resultado = número % 2 # % >> módulo operador que retorna o resto da divisão,
# 0 ou 1, diferente do operador // que é a divisão.
if resultado == 0:
   print('\033[32mEste número é PAR')
else:
  print('\033[31mEste número é ÍMPAR')

