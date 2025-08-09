'''Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import datetime

import os

anodenascimento = int(input("Digite seu ano de nascimento: "))
anoatual = datetime.now().year
idade = anoatual - anodenascimento

if idade < 18:
    print ('Você ainda vai se alistar no Serviço Militar.')
    anos_faltando = 18 - idade
    print (f'Faltam {anos_faltando} anos para o sei alistamento.')
elif idade == 18:
    print ('Você deve se alistar no Serviço Militar.')
else:
    print ('Você passou do prazo de se alistar no Serviço Militar.')
    anos_passados = idade - 18
    print(f'O prazo passou há {anos_passados} ano(s).')


# --- Adição para limpar o terminal ---
input('\n Pressione Enter para limpar o terminal...')

os.system('cls' if os.name == 'nt' else 'clear')
