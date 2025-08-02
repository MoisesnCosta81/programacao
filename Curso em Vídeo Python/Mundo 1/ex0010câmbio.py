carteira = float(input('Quanto você tem na carteira? $ '))
cota = float(input('Cotação do Dollar no dia: R$ '))
real = float(input('Quantos Reais você tem na carteira? R$ '))

print('Com esses ${:.2f} você compra R${:.2f}'.format(carteira, (carteira * cota)))
print('Com esses R${:.2f} você compra ${:.2f}'.format(real, (real / cota)))

