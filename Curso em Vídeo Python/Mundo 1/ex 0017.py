
# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjarcente de um triângulo retângulo, calcule e mostre o
# comprimento da hipotenusa.
# RESOLUÇÃO MATEMÁTICA : Hipotenusa é igual a raiz quadrada da
# soma dos quadrados dos catetos

'''co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjarcente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
print('-'*40)'''

import math
cateto1 = float(input('Cateto oposto: '))
cateto2 = float(input('Cateto adjacente: '))
hipotenusa = math.hypot(cateto1, cateto2)
print('A hipotenusa é: {:.2f}'.format(hipotenusa))

print('-'*50)
