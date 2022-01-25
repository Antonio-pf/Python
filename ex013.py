salario = float(input('Qual o salário do funcionário? R$'))
salario_com_aumento = salario + (salario * 0.15)

print('Um funcionário que ganhava R${}, com um aumento de 15%, passa a receber R${:.2f}'.format(salario, salario_com_aumento))