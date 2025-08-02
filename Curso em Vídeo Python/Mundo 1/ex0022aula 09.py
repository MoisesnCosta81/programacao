'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúscullas.
O nome com todas minúsculas.
Quantas letras ao todo sem considerar os espaços.
Quantas letras tem o primeiro nome.'''
from itertools import count

# Elimina os espaços antes e depois - .strip()
nome = str(input('Qual o seu nome completo? ')).strip()
print('Analisando seu nome...')
print('Seu nome apenas com letras maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome apenas com letras minúsculas é: {}.'.format(nome.lower()))
#remover os espaços iniciais e finais - frase.strip()
#remover os espaços da direita - frase.rstrip()
#remover os espaços da esquerda - frase.lstrip()
print('Seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))
# combinar a função len - conta caracteres, subtraindo com a função .count( ) -
# conta espaço se dentro dos parênteses tiver apenas espaço
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
# split separa em lista
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa [0], len(separa[0])))
#.format(separa [0], lern(separa[0])) - separa[0] é o nome da primeira lista{'###', '##','####', "etc."}
# e o len(separa[0]) é a contagem de caracteres da primeira lista.

