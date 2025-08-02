'''Crie um programa que leia o nome de uma pessoa e
diga se tem "SILVA" no nome.'''

#nome = str(input('Qual o seu nome ? ')).strip()
#print(nome [:].upper == 'SILVA')

#nome = str(input('Qual o seu nome completo? ')).strip()
#print('Seu nome tem Silva? {}'.format(nome[:5] == 'Silva'))

nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
''' in -> um operador do python >>> faz uma busca na variável 'nome' se contém Silva.
no nome.upper ou nome.lower a condição .format('Silva) de estar toda igual conforme
a condição upper ou lower >> SILVA ou silva, não pode Silva pois dará erro, sempre False'''
