print('''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.''')

'''Como calcular o ano bissexto?
Para calcular os anos bissextos, utilizam-se estas regras:
- A cada quatro anos, há um ano bissexto;
- São bissextos todos os anos múltiplos de 400, exceto
se for múltiplo de 100, mas não de 400, por exemplo:
1996, 2000, 2004, 2008, 2012, 2016, 2020;
- Não são bissextos os anos múltiplos de 100.
De acordo com o cálculo, os próximos anos bissextos divisíveis
por 4 serão: 2024, 2028, 2032, 2036, 2040, 2048, 2052.

Para melhor entender
    São bissextos todos os anos múltiplos de 400, p.ex.: 1600, 2000, 2400, 2800...
    São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100
    (ou seja, o último ano de cada século) mas não de 400, p.ex.: 1996, 2000, 2004,
    2008, 2012, 2016, 2020, 2024, 2028...
    Não são bissextos anos ímpares e anos pares não múltiplos de 4.'''

from datetime import date#importa o módulo data ano atual
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year#se o ano for zero considerar o ano atual.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO.'.format(ano))
