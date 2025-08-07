('''Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
 O programa vai perguntar o valor da casa,
 o salário do comprador e
 em quantos anos ele vai pagar.
Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então empréstimo será negado.''')
print()
print('*'*75)
print()

casa = float(input('Qual o valor do imóvel? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quanto anos pretende quitar o imóvel?'))
parcelas = int(anos*12)
prestação = casa/parcelas
print('\033[0;30;43mDe acordo com os dados fornecidos...\033[m\n'
      '\033[0;30;43mPara quitar uma casa de R$ {:.2f} em {:.0f} anos,\033[m' 
      '\n\033[0;30;43mserão necessárias {} parcelas de R$ {:.2f}.\033[m'.format(casa, anos, parcelas, prestação))
if prestação > salário * 0.30:
    print('\033[0;30;41mNestas condições, infelizmente, \033[m\n'
          '\033[0;30;41mnão será possível a aprovação do seu financiamento\033[m\n'
          '\033[0;30;41mpor ultrapassar 30% do seu salário.\033[m')
else:
    print('\033[0;30;42mParabéns! Seu empréstimo foi aprovado!\033[m')

