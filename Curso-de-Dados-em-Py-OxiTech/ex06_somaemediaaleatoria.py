'''Faça um programa que leia 5 números e informe a soma e a média dos números. Os números serão lidos separadamente.'''

import os


soma = 0 #inicializa a soma dos números
numdigitados = []#cria uma lista vazia à ser preenchida pela entrada.
#Loop para ler os 5 números
for c in range(5):
    
    numero = int(input('Digite o {}º número: '.format(c+1)))#Lê um número do usuário

    numdigitados.append(numero)#adicionar o número digitado à lista

    soma = soma + numero

media = float(soma) / 5 
#calculando a média dos números

print('a soma dos números {} é {}; e a media é {}.'.format(numdigitados, soma, media))



# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')

os.system('cls' if os.name == 'NT' else 'clear')

