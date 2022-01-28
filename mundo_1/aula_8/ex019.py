# Sorteio
import random

nome_alunos = []

name = input('Insira o nome do aluno: ')
nome_alunos.append(name)

while name:
    name = input('Insira o nome do aluno: ')
    nome_alunos.append(name)
    print(nome_alunos[:])


print('---------------------------------')
escolhido = random.choice(nome_alunos)
print('O escolhido foi: ', escolhido)
