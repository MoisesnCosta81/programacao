'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto.
- à vista no cartão: 5% de desconto.
- preço normal: em até 2x nop cartão.
- 3x ou mais no cartão: 20% de juros'''

import os
print()
print('{:=^40}'.format('Lojas Costa'))

preco = float(input('Digite o preço: '))
pagamento = int(input('''Digite a forma de pagamento:
    Dinheiro/cheque -- [1]
    Cartão à vista --- [2]
    Cartão até 2x ---- [3]
    Catão 3x ou mais --[4]'''))

avista = preco - (0.10 * preco)
avistacartao = preco - (preco * 0.05)
duasvezescartao = preco
maisdetresvezes = preco + (preco * 0.20)


if pagamento == 1:
    print('\nPagamentos à Vista você tem 10% de descoto, o preço será : R$ ', avista,'.')

elif pagamento == 2:
    print('\nPagamentos no cartão à vista tem 5% de desconto, o preço será: R$ ', avistacartao,'.')

elif pagamento == 3:
    print('\nPagamentos no cartão em até 2x tem preço de à vista, o preço será: R$ ',duasvezescartao, 'em 2 parcelas de R$',duasvezescartao / 2,'.')

elif pagamento == 4:
    
    nparcelas = int(input('Quantas parcelas? '))
    parcelas = maisdetresvezes / nparcelas
    print('\nPagamentos no cartão em 3x ou mais terão acréscimos de 20%; o preço final ficará em: R$ ',maisdetresvezes,'.')
    print('Sua compra será parcelada em', nparcelas,'x de R$ ', parcelas, '.')

else:
    print('\n\033[31mOpção inválida. Digite as opções de 1 à 4.\033[m')

# --- Adição para limpar o terminal ---
input('\nDigite enter para limpar o terminal...')

os.system('cls' if os.name == 'NT' else 'clear')
