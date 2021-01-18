from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
 [0] pedra
 [1] papel
 [2] tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')
