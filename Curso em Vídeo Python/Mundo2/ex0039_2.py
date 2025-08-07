
from datetime import datetime
import os

atual = datetime.now().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} e tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você terá que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
    
elif idade > 18:
    saldo = idade -18
    print('Você já deveria ter se alistado há {} ano(s)'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
    

# --- Adição para limpar o terminal ---
input('\n Pressione Enter para limpar o terminal...')

os.system('cls' if os.name == 'nt' else 'clear')

