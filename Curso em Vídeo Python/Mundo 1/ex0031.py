print('''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.''')
print('-=-'*25)

distância = float(input('Qual a distância até o destino? '))
print('Em breve a sua viagem de {}Km será iniciada.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('\033[33mA sua passagem custará R${:.2f}'.format(preço))

