n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))

m = (n1 + n2)/ 2

if m < 5:
    print('Reprovado: {}'.format(m))
elif 7 > m >= 5:
    print('Recuperação: {}'.format(m))
elif m >= 7:
    print('Aprovado: {}'.format(m))