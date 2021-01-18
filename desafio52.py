n = int(input('Entre com o numero para saber se ele é primo ou não: '))
tot = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
if tot == 2:
    print('Ele é Primo!')
else:
    print('Não é primo.')