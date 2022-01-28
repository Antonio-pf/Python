dias_alugado = int(input('Quantos dias alugado? '))
km_precorrido = int(input('Quantos Km percorridos? '))
valor_do_aluguel = (dias_alugado*60) + (km_precorrido*0.15)

print('O total a pagar é: R${:.2f}'.format(valor_do_aluguel))
