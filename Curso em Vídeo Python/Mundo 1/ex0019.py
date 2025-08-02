# Um professor quer sortear um de seus
# quatro alunos para apagar o quadro. Faça um pograma que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido é: {}'.format(escolhido))
print('#'*75)
