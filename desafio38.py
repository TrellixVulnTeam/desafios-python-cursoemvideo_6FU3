x = int(input('Entre com o primeiro valor: '))
y = int(input('Entre com o segundo valor: '))

if x > y:
    print('{} maior que {}'.format(x, y))
elif y > x:
    print('{} maior que {}'.format(y, x))
else:
    print('{} e {} são iguais'.format(x, y))