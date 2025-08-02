print('''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem que ele foi multado.
A multa vai custar R$7,00 por cada km/h acima do limite.''')
print('-=-' * 25)

velocidade = float(input('Qual a velocidade atual do carro?:  '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h.')
    multa = (velocidade - 80) * 7
    print('Você pagará uma multa de R${:.2f}!'.format(multa))
print('\033[33mTenha um bom dia! Dirija com segurança!')

#print(\033[0;30;41m) padrão de código de cores
#print(\033[;33;44m)
#print(\033[1;35;43m)
#print(\033[30;42m)
#print(\033[m)
#print(\033[7;30m)