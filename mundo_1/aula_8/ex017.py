# Hipotenusa
from math import hypot
cat_oposto = float(input('Digite o cateto oposto: '))
cat_adjacente = float(input('Digite o cateto adjacente: '))
hip = hypot(cat_oposto, cat_adjacente)

print('Comprimento da hipotenusa: {:.2f}'.format(hip))

