t = float(input('Qual a temperatura em C°? '))
f = (t * 9) / 5 + 32
print('Esta temperadtura corresponde a {:.1f}F°'.format(f))
t2 = float(input('Qual a temperatura em F°? '))
c = (t2 - 32) * 5 / 9
print('Esta temperatura corresponde a {:.1f}C°'.format(c))

