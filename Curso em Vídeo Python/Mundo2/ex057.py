'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente até um valor correto.'''


sexo = str(input("Informe seu sexo[M/F]: ")).strip().upper()[0]#strip tira os espaços e upper coloca tudo pra maiúsculo e 0 [0] pega a primeira letra
while sexo not in 'MmFf':#função not in pra dizer que enquanto sexo não for MnFf...
    sexo = str(input('Dados inválidos. Por favor digite seu sexo: ')).strip().upper()[0]
print(f"Seu sexo é {sexo} e foi registrado com sucesso!")

idade = int(input('Digite a sua idade: '))
