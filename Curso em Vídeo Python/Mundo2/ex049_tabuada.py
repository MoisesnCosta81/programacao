'''Refaça o desafio 9, mostrando a tabuada de um número que usuário escolher, só que agora utilizando um laço for.'''

import os

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))



# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')
os.system('cls' if os.name == 'NT' else 'clear')
