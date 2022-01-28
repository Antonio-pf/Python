#Discrições da variável
algo = input('Ditite algo: \n')
print('\n-----------Dissecando------------\n')
print('Você digitou: {}'.format(algo))
print('Variável do tipo: ',type(algo))
print('É númerica?--->{}'.format(algo.isnumeric()))
print('É alfa númerica?--->{}'.format(algo.isalnum()))
print('É alfabético?--->{}'.format(algo.isalpha()))
print('É minúscula?--->{}'.format(algo.islower()))
print('É maiúscula?--->{}'.format(algo.isascii()))
print('É decimal?--->{}'.format(algo.isdecimal()))
print('Tem espaço?--->{}'.format(algo.isspace()))

