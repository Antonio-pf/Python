# calcula viagem
import emoji
resposta = str(input(emoji.emojize('E aí:sunglasses:? vai viajar hoje? ', use_aliases=True))).strip().capitalize()


if 'Sim' in resposta:
    distancia = float(input('Qual a distância da viagem?: '))
    if distancia >= 200.0:
        print('Prepara o bolso, terá que pagar: ${}'.format(distancia * 0.45))
    else:
        print('Boa viagem, e lembre-se de levar ${} para custo no percurso!'.format(distancia * 0.5))
else:
    print(emoji.emojize("Você merece viajar, pense nisso :zany_face:", use_aliases=True ))


