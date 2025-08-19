'''Escreva um programa em python que solicite ao usuário um número inteiro positivo. Em seguida, utilize uma estrutura de repetição para exibir a contagem regressiva a partir desse número até zero, pulando de dois em dois.'''

import os

numero = int(input('Digite um número inteiro e positivo: '))

if numero >= 0:
    print(f'\nA contagem regressiva do {numero} pulando de 2 em 2 é:')
    for c in range(numero, -1, -2):
            print(c)
else:
    print('entrada inválida! digite um número inteiro positivo!')        

# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')

os.system('cls' if os.name == 'NT' else 'clear')
