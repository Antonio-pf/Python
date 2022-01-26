import math

angulo = float(input('Digite o ângulo: '))

cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
seno = math.sin(math.radians(angulo))

print('Valor do cosseno de {}º é: {:.3f}'.format(angulo, cosseno))
print('Valor da tangente de {}º é: {:.3f}'.format(angulo, tangente))
print('Valor do seno de {}º é: {:.3f}'.format(angulo, seno))
