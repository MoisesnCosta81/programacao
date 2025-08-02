# Manipulando texto

# >>>>> Fatiamento:

frase = 'Curso em Vídeo Python'
frase[9]
print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#>>>>>Análise
#função Len - comprimento, contagem
#count('o') - contar quantas vezes aparece o caractere dentro das aspas
#count('o',0,13) - contagem com fatiamento - considera do 0 até o 12 quantas letras o
#find('deo') - quantas vezes existe deo
#find('Android') - quando não existe exibe -1
#in - 'Curso' in frase - Operador falso ou verdadeiro

#* Transformação
#frase.replace('Python', 'Android') - substitui um pelo outro
#frase.upper() - troca para tudo maiúsculo
#frase.lower() - troca por tudo minúsculo
#frase.capitalize() - muda tudo pra minúsculo menos a primeira letra
#frase.title() - muda apenas as primeira letras para maiúsculo
#frase.strip() - remove espaços inúteis, início e fim da frase
#frase.rstrip() - remove apenas os últimos espaços - direita
#frase.lstrip() - remove apenas os espaços da esquerda - início

#*Divisão
#frase.split() - criará divisão e nova lista com cada palavra - divide str em lista - cada palavra vira lista

#*Junção
#'-'.join(frase) - coloca ífen(-) onde tem espaços
