##Conversão de medidas
medida = float(input('Digite uma medida em metros:\n'))
print('A medida {}M corresponde a: '.format(medida))
print('{}Km'.format(medida/1000))
print('{}hm'.format(medida/100))
print('{}dam'.format(medida/10))
print('{}dm'.format(medida*10))
print('{}cm'.format(medida*100))
print('{}mm'.format(medida*1000))

##OU
print()
medida = float(input('Digite uma medida em metros:\n'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('{}Km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))