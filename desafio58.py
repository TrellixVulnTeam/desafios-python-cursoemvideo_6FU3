from random import randint
computador = randint(0, 10)
cont = 1
jogador = int(input('Tente adivinhar o valor selecionado pela maquina: '))
while jogador != computador:
    cont += 1
    print('Errrrou, tente novamente.')
    jogador = int(input('Tente adivinhar o valor selecionado pela maquina: '))
print('-----------------------------------------')
print('Acertou! Foram necessarias {} tentativas.'.format(cont))
