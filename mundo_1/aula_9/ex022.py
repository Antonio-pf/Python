# tudo maiuscula
# td minus
# qbdt letras sem espaço
# qntd o primeiro nome

nome_completo = str(input('Digite seu nome completo: ')).strip()
qntd_sem_espaço = (len(nome_completo)) - nome_completo.count(' ')
primeiro_nome = len(nome_completo.split().pop(0))

print('Nome todo maiúsculas: {}'.format(nome_completo.upper()))
print('Nome todo minúsculas: {}'.format(nome_completo.lower()))
print('Quantidade de LETRAS sem espaço: {}'.format(qntd_sem_espaço))
print('Quantidade de LETRAS no primeiro nome: {}'.format(primeiro_nome))

'''correção com maneira simples'''
print('Quantidade de LETRAS sem espaço: {}'.format(len(nome_completo) - nome_completo.count(' ')))
print('Quantidade de LETRAS no primeiro nome: {}'.format(nome_completo.find(' ')))

