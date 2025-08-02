print('''Desenvolva um programa que leia o coomprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.''')
print('\033[33m#'*75)
print('Analisador de Triângulos')
print('\033[33m#'*75)

r1 = float(input('\033[mPrimeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mCom esses seguimentos é possível fazer um triângulo.')
else:
    print('\033[31mCom esses seguimentos não é possível fazer um triângulo.')

