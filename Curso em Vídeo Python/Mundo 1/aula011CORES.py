'''Cores no terminal'''
#padrão ANSI

'''
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m
'''

print('\033[31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m') #desfazer cores para a barra não ficar até o final
print('\033[29;45mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')

nome = str(input('Qual o seu nome? '))
print('Olá! Muito prazer em te conhecer, {}!!!'.format(nome))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[7;29m', nome, '\033[m'))

