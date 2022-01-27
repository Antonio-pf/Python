# verifica qualquer posição
nome = str(input('Digite seu nome inteiro: ')).strip()

encontre = nome.find('Silvia')

if encontre > 0:
    print('Tem SILVIA no nome')

else:
    print('Não tem SILVIA nome')

# outra maneira

nome1 = str(input('Digite seu nome inteiro: ')).strip().title()

encontre1 = "Silvia" in nome1
print(encontre1)

# maneira feita em aula

nome2 = str((input('Qual seu nome completo')).strip())
print('Seu nome tem Silva?: {}'.format('Silva' in nome2.capitalize()))




















