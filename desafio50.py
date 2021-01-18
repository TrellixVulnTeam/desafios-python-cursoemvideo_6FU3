soma = 0
cont = 0
for i in range(1,7):
    n = int(input('Entre o {} valor: '.format(i)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Voce informou {} numeros PARES e a soma foi {}.'.format(cont, soma))