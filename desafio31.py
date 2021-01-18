d = float(input('Entre com a distancia percorrida: '))
if d <= 200:
    x = d*0.50
    print('Voce deve pagar {}'.format(x))
else:
    x = d*0.45
    print('Voce deve pagar {}'.format(x))