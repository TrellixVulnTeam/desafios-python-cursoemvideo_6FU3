from datetime import date
today = date.today().year
cont = 0
for i in range(1, 8):
    nasc = int(input('Entre com {} ano do nascimento: '.format(i)))
    if today - nasc < 18:
        cont = cont + 1
print('{} menores de idade'.format(cont))
