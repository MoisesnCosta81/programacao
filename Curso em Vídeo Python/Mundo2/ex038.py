'''Ecreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais'''


n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2 :
    print ('O PRIMEIRO número é maior que o número {}.'.format(n2))

elif n2 > n1 :
    print ('O SEGUNDO número é maior que o número {}.'.format(n2))
else :
    print('Não existe nenhum valor maior, os dois números são IGUAIS.')

