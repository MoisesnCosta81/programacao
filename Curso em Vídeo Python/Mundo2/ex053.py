'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = str(input("Digite uma frase: ")).strip().upper() #entrada
palavras = frase.split() #dividir as palavras sem os espaços.
junto = ''.join(palavras)#juntar as palavras sem espaço.
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')
