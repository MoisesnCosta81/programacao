d = float(input('Quantos dias? '))
km = float(input('Quantos Km rodados? '))
vdia = d * 60.0
vkm = km * 0.15
valor = vdia + vkm
print('O valor a pagar pelo aluguel de {:.2f} dias e {:.2f}km rodados será de: R$ {:.2f} '.format(d, km, valor))

