name = input('Digite seu nome: ')
print('Prazer', name)
#outro modo para formatar e dar espaços etc.
print('Prazer {}!'.format(name))
#arredondando com format
number = 123.32
number2 = 265.4963
print(number * number2)
print('<---Arredondamento para duas casa--->')
result = number * number2
print('{:.2f}'.format(result))
print('{:.3f}'.format(result))
print('{:.4f}'.format(result))