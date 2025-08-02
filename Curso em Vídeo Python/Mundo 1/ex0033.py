print('''Faça um programa que leia três números
e mostre qual é o MAIOR e qual é o MENOR.''')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número digitado foi: {}.'.format(menor))
print('O maior número digitado foi: {}.'.format(maior))
