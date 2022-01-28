from builtins import print

n1 = int (input('Digite um número: '))
n2 = int (input('Digite um número: '))
s = n1 + n2
print('A soma', s)
div = s % 2
print(div)
#outra maneira de saida
print('A soma vale{}   '.format(s))