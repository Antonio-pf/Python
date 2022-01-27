##Verifica um nome no começo
nome_da_cidade = str(input('Digite o nome da cidade: ')).strip().capitalize()
verifica = "Santo" in nome_da_cidade
print(verifica)

##outro modo pela aula da aula
nome = str(input('Digite o nome da cidade')).strip()
print(nome[:5].upper() == "SANTO")



