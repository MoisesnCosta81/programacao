'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novo números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
import time
from time import sleep
import sys

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa.''')
    opção = int(input('>>>>>>> Qual a sua opção? <<<<<<<\n'))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual à {soma}.')

    elif opção == 2:
        mult = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é igual à {mult}')

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre o {n1} e o {n2} o maior valor é {maior}')

    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opção == 5:
        time.sleep(1)
        print('Finalizando ', end='')
        for _ in range(3):
            print(".", end='', flush=True)
            time.sleep(1)
    else:
        print('Opção inválida. Digite entre 1 e 5!')

print('\nFim do programa! Volte sempre!')

