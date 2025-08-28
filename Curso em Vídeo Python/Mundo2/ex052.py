'''Faça um programa que leia um número interio e diga se ele é ou não um número primo.'''

n = int(input("Digite um número inteiro: "))
vzs = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        vzs += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, vzs))
if vzs == 2:
    print('É número É PRIMO!')
else:
    print('Este número NÃO é PRIMO.')
