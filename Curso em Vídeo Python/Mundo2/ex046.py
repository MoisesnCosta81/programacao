'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo sentre eles.'''

import os
from time import sleep


for contagem in range(10, 0, -1):
    sleep(1)
    print(contagem)
    
sleep(1)   
print ('FELIZ ANO NOVO!')
emojifogos = "\U0001F389"
print(emojifogos*10)


# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')

os.system('cls' if os.name == 'NT' else 'clear')
