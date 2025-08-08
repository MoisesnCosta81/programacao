'''a confederação nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: MIRIM
- Até os 14 anos: INFANTIL
- Até os 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''

import os
from datetime import datetime


ano = int(input('Digite seu ano de nascimento: '))
anoatual = datetime.now().year
idade = anoatual - ano

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificado como: MIRIM')

elif idade > 9 and idade <= 14:
    print('Classificado como: INFANTIL')

elif idade > 14 and idade <= 19:
    print('classificado como: JÚNIOR')

elif idade == 20:
    print('Classificado como: SÊNIOR')

else:
    print('Classificado como: MASTER')


   # --- Adição para limpar o terminal ---
input('\n Pressione Enter para limpar o terminal...')

os.system('cls' if os.name == 'nt' else 'clear')
