'''Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "SANTO".'''

print('Vou te dizer se sua palavra tem Santo no começo.')
cid = str(input('Em qual cidade você nasceu? ')).strip()
print(cid[:5].upper() =='SANTO')
'''.Strip -> retira os espaços do input.
.upper -> muda os caracteres do input para maiúsculo
[:5] faz o programa ler até o útimo caractere'''
