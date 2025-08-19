'''Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.'''

import os

for c in range(1, 51, 2):
    print(c,end=',')#end=',' printa lista do lado separado por ,


# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')
os.system('cls' if os.name == 'NT' else 'clear')