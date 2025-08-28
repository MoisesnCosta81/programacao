'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual = date.today().year#Para identificar o ano atual, importa-se a
                         # biblioteca DATETIME e utiliza o recurso DATE.TODAY().YEAR

totalmaior = 0
totalmenor = 0

for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
    idade = atual - nasc

    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor +=1

print(f'Ao todo tivemos {totalmaior} pessoas maiores e {totalmenor} pessoas menores de idade.')
