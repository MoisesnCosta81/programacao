'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.
Ex.: Digite um número: 1834
Unidade: 4
dezena: 3
centena: 8
milhar: 1'''

'''
num = int(input('Digite um número: '))
n = str(num).strip()
# .strip() para eliminar possíveis espaços no input
# converter o número inteiro em str para que seja possível apontar as posições dos caracteres
print('analisando o número digitado: {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
Nesse formato caso o input tenha menos digitos que 4 dá erro'''

num = int(input('Digite um número: '))
u = num // 1 % 10
# %10 - módulo 10 - elimina a milhar, centena e dezena, printa apenas a unidade, sucessivamente.
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número digitado: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

