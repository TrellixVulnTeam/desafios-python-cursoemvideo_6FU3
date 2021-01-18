import math
x = int(input('Entre com o valor do cateto oposto: '))
y = int(input('Entre com o valor do cateto adjacente: '))

h = (math.hypot(x,y))
print('O valor da hipotenusa é {:.2f}'.format(h))