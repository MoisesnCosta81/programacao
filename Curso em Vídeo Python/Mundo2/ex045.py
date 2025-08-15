'''Crie um programa que faça o computador jogar jokenpô contigo.'''

import os
from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0,2)
#print('O computador escolheu {}'.format(itens[computador]))
print(''' Suas opções são: 
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print(KEN)
sleep(1)
print(PÔ)
sleep(1)
print('*'*20)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('*'*20)
if computador == 0: #cpu jogou pedra
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('Jogada inválida!')

elif computador == 1: #cpu jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('Jogada inválida!')

elif computador == 2: #cpu jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATOU!')

    else:
        print('Jogada inválida!')


# --- Adição para limpar o terminal ---
input('\n Pressione Enter para limpar o terminal...')

os.system('cls' if os.name == 'nt' else 'clear')
