maior = 0
menor = 0
for i in range(1, 6):
    p = float(input('Entre com o {} peso: '.format(i)))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

print('{} é o maior peso'.format(maior))
print('{} é o menor peso'.format(menor))