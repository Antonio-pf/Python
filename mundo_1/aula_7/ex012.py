preco = float(input('Qual o preço do produto? R$'))
preco_com_desconto = preco - (preco * 0.05)

print('O produto que custava R${}, na promoção de 5% vai custar R${:.2f}'.format(preco, preco_com_desconto))