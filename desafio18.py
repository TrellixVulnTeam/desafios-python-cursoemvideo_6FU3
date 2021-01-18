from math import radians, sin, cos, tan
x = int(input('Entre com o valor do Angulo: '))
seno = sin(radians(x))
cosseno = cos(radians(x))
tangente = tan(radians(x))
print('O valor do seno desse angulo é: {:.2f}'.format(seno))
print('O valor do cosseno desse angulo é: {:.2f}'.format(cosseno))
print('O valor da tangente desse angulo é: {:.2f}'.format(tangente))
