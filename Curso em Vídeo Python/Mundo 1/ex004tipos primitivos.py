'''print(f'\033[92mO tipo primitivo é: \033[93m{type(n)}\033[0m')
Nesse exemplo:
- \033[92m define a cor do texto para verde (para "O tipo primitivo é: ")
- \033[93m define a cor do texto para amarelo (para o tipo primitivo)
- \033[0m restaura a cor padrão do terminal'''

n = input('digite algo: ')
print('O tipo primitivo é:', type(n))
print(f'\033[92mO tipo primitivo é: \033[93m{type(n)}\033[0m')
#usando f'' e colocando o {type(n)} entre chaves e tudo entre as aspas do f é possível colorir.
# Com o f eu funcionalizo o conteúdo independente se str ou variável
print('Só tem espaços?', n.isspace())
print(f'\033[7;31mSó tem espaços? {n.isspace()}\033[m')
print(f'É um número?, \033[7;31m{n.isnumeric()}\033[m')
print('É alfa?', n.isalpha())
print('É apenas alfanumérico?', n.isalnum())
print('Está maiúsculo?', n.isupper())
print('Está minúsculo?', n.islower())
print('Está capitalizada?', n.istitle())

