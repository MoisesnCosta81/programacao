'''Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas.
No final do programa, mostre:
A média de idade do grupo.
Qual éo nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 6):
    print(f'----- {p}ª PESSOA ----.')
    nome = str(input('Nome: ')).strip()#strip tira os espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 5
print(f'A idade média do grupo é de {mediaidade} anos.')
print(f'O home mais velho se chama {nomevelho} e tem {maioridadeh} anos.')
print(f'Exitem na lista {totmulher20} mulheres abaixo de 20 anos.')
