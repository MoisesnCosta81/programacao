'''Escreva um programa que leia um número qualquer e peça para o usuário escolher qual a base
de conversão: - 1 para binário
              - 2 para octagonal
              - 3 para hexadecimal'''


import os
num = int(input('Digite um número:'))
print('''Você deseja converter esse número para:
\033[33mBINÁRIO\033[m? Digite [1]
\033[36mOCTAGONAL\033[m? Digite [2].
\033[32mHEXADECIMAL\033[m? Digite [3].''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('\033[33mO número {} convertido para BINÁRIO é igual a {}.\033[m'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('\033[36mO número {} convertido para OCTAGONAL é igual a {}.\033[m'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('\033[32mO número {} convertido para HEXAGONAL é igual a {}.\033[m'.format(num, hex(num)[2:]))
    #bin() / oct() e hex() transformam o referido número nas respectivas bases; binário, octagonal e hexadecimal
    #[2:] eliminar os dois primeiros dígitos
else:
    print('\033[31mOpção inválida! Escolha apenas de 1 a 3.\033[m')

