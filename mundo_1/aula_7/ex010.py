dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))

##0.1807 Dollar proporcional a 1R$
converte = dinheiro * 0.1807
print('Com {}R$ você pode comprar US${:.2f}'.format(dinheiro, converte))
