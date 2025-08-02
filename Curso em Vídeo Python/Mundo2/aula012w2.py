nome = str(input('Qual o seu nome? '))
if nome == 'Moisés':
    print('Que nome bonito!')
elif nome == 'Natanael' or nome == 'João' or nome == 'Gabriel' or nome == 'Glaucyanna':
    print('Seu nome também é muito lindo e bem popular! Parabéns {}!'.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem comum!')
print('Tenha um bom dia, \033[7;29m{}\033[m!'.format(nome))
print('*'*75)
