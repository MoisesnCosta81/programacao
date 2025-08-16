'''Desenvolva um programa queleia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa prograssão.'''

import os

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1) * razao #fómula matemática para achar o 10º termo de uma PA
for pa in range(primeiro, decimo + razao, razao): #decimo+razao para exibir o 10º termo
#substituiu as três variáveis da estrutura for ex: for n in range(1, 11, 2): intervalo 1, 11 -- razão ,2(no caso aleatória).

    print('{}'.format(pa),end=' --> ')
print('FIM!')


# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')
os.system('cls' if os.name == 'NT' else 'clear')