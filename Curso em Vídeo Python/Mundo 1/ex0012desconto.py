p = float(input('Qual preço do produto? R$ '))
desc = p * 5/100
pdesc = p - desc
print('Com o desconto de 5% este produto de R${:.2f} ficará por R${:.2f}'.format(p, pdesc))

    