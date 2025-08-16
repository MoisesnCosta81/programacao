'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 - 50.'''

import os

for intervalo in range(1, 51):
    #print(intervalo)
    if intervalo % 2 == 0:
        print(intervalo, end=' ')

print('FIM!')

# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')

os.system('cls' if os.name == 'NT' else 'clear')
