m = float(input('A medida em metros é: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('\033[7;30;43mEsta medida de metros em kilômetros é: {}km'.format(km))
print('Esta medida de metros em Hectômetros é: {}hm'.format(hm))
print('Esta medida de metros em Decâmetros é: {}dam'.format(dam))
print('Esta medida de metros em Decímetros é: {}dm'.format(dm))
print('Esta medida de metros em Centímetros é: {}cm'.format(cm))
print('Esta medida de metros em mm é: {}mm'.format(mm))
