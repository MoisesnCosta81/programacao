print('''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.''')
print('#'*75)

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
'''.format(frase.find('A')+1)) -- Ao colocar o recurso +1 após o .find('A') o programa exibe
 a posição conforme a observação e não coforme a contagem real do programa que inicializa-se
na posição 0 zero.
a função .find realiza busca por caractere.
rfind realiza a busca a partir do lado direito.
'''
