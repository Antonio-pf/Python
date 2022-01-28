# é ano bissexto?
from calendar import isleap

ano = int(input('Qual ano você está? '))

if isleap(ano):
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto')
