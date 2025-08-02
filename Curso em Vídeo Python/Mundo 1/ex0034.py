print('''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais o aumento é de 15%.''')
print('&'*50)

salário = float(input('Qual o salário? R$ '))
if salário <= 1250.00:
    ajuste = salário + (salário * 0.15)
else:
    ajuste = salário + (salário * 0.10)
print('Quem ganhava \033[31mR$ {} \033[mpassa a ganhar o novo salário de: \033[32mR$ {}.'.format(salário, ajuste))
