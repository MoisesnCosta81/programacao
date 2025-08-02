s = float(input('Qual o salário? R$ '))
aumento = s * 15/100
novosal = s + aumento
print('Um funcionário com o salário de R${:.2f} com um aumento de 15% receberá R${:.2f}. Um ganho de R${:.2f}'.format(s, novosal, aumento))

    