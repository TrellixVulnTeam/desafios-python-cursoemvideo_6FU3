x = int(input('Entre com o primeiro valor: '))
y = int(input('Entre com o segundo valor: '))
z = int(input('Entre com o terceiro valor: '))

menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z

maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z

print('O menor valor é: {}'.format(menor))
print('O maior valor é: {}'.format(maior))