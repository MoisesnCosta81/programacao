nome1 ='Moisés'
idade1 = 25
peso1 = 89.8
print(nome1, idade1, peso1)
print('*'*75)

nome = input('Qual é seu nome? ')
idade = input('Qual a sua idade? ')
peso = input('Qual o seu peso? ')
print(nome,',', idade,',', peso,'.')
#print(f"{nome}, {idade}, {peso}.") >> neste modelo de print é possível por cor nas variáveis
print(f"\033[91m{nome}, {idade}, {peso}.\033[m")
print('*'*75)

nome = input('Qual o seu nome? ')
print('Olá', nome, 'é um prazer te conhcer!')
idade = input('Me fala qual a tua idade? ')
peso = input('Hum... Entendi. Qual o seu peso? ')
print('\033[0;30;42mEntão você tem', idade, 'anos e pesa', peso, 'kg.\033[m')
print('*'*75)