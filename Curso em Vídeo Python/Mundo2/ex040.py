'''Crie um programa que leia duas notas de uma aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado'''
import os

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2

if media < 5:
    print(f'Com as notas {n1} e {n2} a sua média foi {media} - \033[31mREPROVADO\033[m')
elif media >= 5 and media < 7:
    print(f'Com as notas {n1} e {n2} a sua média foi {media} - \033[33mRECUPERAÇÃO\033[m')
else:
    print(f'Com as notas {n1} e {n2} a sua média foi {media} - \033[32mAPROVADO\033[m')

    # --- Adição para limpar o terminal ---
input('\n Pressione Enter para limpar o terminal...')

os.system('cls' if os.name == 'nt' else 'clear')


