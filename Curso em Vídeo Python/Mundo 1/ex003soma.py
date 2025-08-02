n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
#print('a soma de', n1, '+', n2, 'é igual a:', s)
print('\033[0;30;41mA soma de {} + {} é igual a: {}\033[m'.format(n1, n2, s))

