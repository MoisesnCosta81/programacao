n = float(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** 0.5
print()
print('Observando o valor digitado, \no dobro é \033[32m{}\033[m, \no triplo é \033[31m{}\033[m \ne a raiz quadrada é \033[30;41m{:.2f}\033[m'. format(d, t, r))

#\n quebra a linha no print