import random
numero = random.randint(0,5)
adiv = str(input('Tente adivinhar o numero escolhido pelo computador, entre 0 e 5: '))
if adiv == numero:
    print('Parabens, voce acertou')
else:
    print('Vish, voce errou')
