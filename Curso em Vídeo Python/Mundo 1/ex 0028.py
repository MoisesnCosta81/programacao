print('''Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir ual foi o número
escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu''')

from random import randint #importar biblioteca de randomização de número inteiro.
from time import sleep # importa biblioteca time função sleep parecido com pausa

computador = randint(0, 5) #Faz o computador 'PENSAR'
#print('Pensei no número {}.'.format(computador)) # linha de teste, não pode aparecer
print('-=-' * 25)
print('Vou pensar em um número de 0 à 5. Tente adivinhar...')
print('-=-'*25)
print('PENSANDO...')
sleep(1)
jogador = int(input('Em que número eu pensei? ')) # o jogador tenta adivinhar
if jogador == computador:
    print('Parabéns! Você venceu!')
else:
    print('Ganhei! eu pensei no número {} e não no número {}!'.format(computador, jogador))
    #U+1F60E
    print('\U0001F60E') # precisa modificar o código do emoji pra printar.

