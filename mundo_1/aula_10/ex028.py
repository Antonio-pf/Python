# Advinha
from random import randint
n = randint(0, 5)
print(n)

print('Pensei em um número de 0 a 5!')
print('Chuta aí, qual você acha que é!?: ')
chute = int(input('Seu chute------->  '))

if chute == n:
    print('Caraca, você acertou!')
else:
    print('Não foi dessa vez em...quem sabe na próxima!')


