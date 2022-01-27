# sorteio ordem para apresentação
from random import shuffle

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('Ordem da apresentação')
print(lista)


