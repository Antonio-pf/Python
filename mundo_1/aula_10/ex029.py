velocidade = float(input('Fala pra mim a velocidade máx: '))
valor_multa = 0.0

if velocidade > 80:
    valor_multa = (velocidade - 80) * 7
    print('Você foi multado e pagará: ${:.2f}'.format(valor_multa))
else:
    print('Continue assim, dirigindo com segurança')