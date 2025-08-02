print('''Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.
 Ex.: Ana maria de souza
 Primeiro nome = Ana
 Último nome = Souza''')

n = str(input('Qual o seu nome completo? ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('O primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
'''função len conta/identifica as listas geadas pela função .split; por isso
a variável n foi condicionada >> nome = n.split'''
