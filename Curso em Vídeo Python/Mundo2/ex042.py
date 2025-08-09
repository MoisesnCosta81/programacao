'''Desenvolva um programa que leia o coomprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'\033[33m#'*75
'Analisador de Triângulos'
'\033[33m#'*75

Reforçar o desafio 35 dos triângulos acrescentando o recurso de mostrar
 que tipo de triângulo será formado:
 - Equilátero: Todos os lados iguais.
 - Isósceles: dois lados iguas.
 - Escaleno: Todos os lados diferentes'''
import os

r1 = float(input('Digite o cumprimento da primeira reta: '))
r2 = float(input('Digite o cumprimento da segunda reta: '))
r3 = float(input('Digite o cumprimento da terceira reta: '))

if (r1 < (r2 + r3)) and (r2 < (r1 + r3)) and (r3 < (r1 + r2)):
    print('\nCom essas medida é possível fazer um triângulo ', end='')

    if r1 == r2 == r3:
        print('Equilátero, pois possui todos os lados com a mesma medida.')

    elif r1 != r2 != r3 != r1:
        print('Escaleno, pois possui todos os lados de diferentes medidas.')

    else:
        print('Isósceles pois possui dois lados de medidas iguais.')

else:
    print('Não é possível formar um triângulo com essas medidas!')



# --- Adição para limpar o terminal ---
input('\n Pressione Enter para limpar o terminal...')

os.system('cls' if os.name == 'nt' else 'clear')

