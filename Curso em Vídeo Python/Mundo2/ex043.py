'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal.
- De 25 até 30: Sobrepeso.
- De 30 até 40: Obesidade.
- Acima de 40: Obesidade mórbida'''

import os

peso = float(input('Digite qual o seu peso: '))
altura = float(input('Digite qual a sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('\nAbaixo do peso.')

elif imc < 26:
    print('\nPeso ideal.')

elif imc < 31:
    print('\nSobrepeso.')

elif imc < 41:
    print('\nObesidade.')

else:
    print('\nObesidade Mórbida')


# --- Adição para limpar o terminal ---
input('\n Pressione Enter para limpar o terminal...')

os.system('cls' if os.name == 'nt' else 'clear')
