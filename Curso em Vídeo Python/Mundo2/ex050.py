'''Desenvolva um programa que leia seis números interios e mostre a soma apenas daqueles forem pares. Se o valor digitado for impar, desconsidere-o.'''

import os

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma)) 

# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')
os.system('cls' if os.name == 'NT' else 'clear')
