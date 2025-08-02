altura  = float(input('Qual a altura? '))
comprimento = float(input('Qual a comprimento    ? '))
área = altura * comprimento
print('A área da parede é de {:.2f}m\u00B2'.format(área))
print('Serão necessário {:.2f}L de tinta para cobertura da área.'.format(área/2))
tinta = área / 2
print('Serão necessário {:.2f} litros de tinta para cobertura desta área.'.format(tinta))

#m\u00B2 >>> m² no print
