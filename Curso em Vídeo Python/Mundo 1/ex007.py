n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota'))
m = (n1 + n2)/2
print('Analisando a primeira nota \033[0;30;44m{}\033[m e a '
      'segunda nota \033[0;30;43m{}\033[m, '
      'a média é \033[7;29;40m{:.2f}\033[m'.format(n1, n2, m))

