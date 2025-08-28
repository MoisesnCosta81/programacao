'''Melhore o jogo do desafio 28 onde o computador vai "pensar" num múmero entre 0 e 10
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.'''

from random import randint
computador = randint(1,10)#variável de aleatoriedade de 0 a 10.
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.\nSerá que você adivinha qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpite} tentativas.')

