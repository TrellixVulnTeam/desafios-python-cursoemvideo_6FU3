import math
print('opções de bases de conversão: 1-Binário; 2- Octal; 3- Hexadecimal')
b = int(input('Em qual base deseja converter?'))
x = int(input('Entre com o numero que deseja converter: '))

if b == 1:
    print('{} covertido para binário é igual a: {}'.format(x, bin(x)))
elif b == 2:
    print('{} covertido para octal é igual a: {}'.format(x, oct(x)))
elif b == 3:
    print('{} covertido para hexadecimal é igual a: {}'.format(x, hex(x)))
else:
    print('Valor não reconhecido: ')