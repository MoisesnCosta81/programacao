'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 e 500.'''

import os

s=0 #acumulador
cont=0 #contador
for c in range(1,501, 2):
    if c % 3 == 0:
        s = s + c #acumulador a 'variável' do for -- s =+ c
        cont = cont + 1 #contador geralmente é mais 1 -- cont =+ 1
        
print('A soma de todos os {} múltiplos de 3 é {}.'.format(cont, s))




# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')

os.system('cls' if os.name == 'NT' else 'clear')