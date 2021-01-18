somaidade = 0
mediaidade = 0
hvelho = 0
hvelhonome = ''
mnovas = 0
for x in range(1, 5):
    print('-----{}ª Pessoa-----'.format(x))
    n = str(input('Entre com a nome: ')).upper()
    i = int(input('Entre com a idade: '))
    s = str(input('Entre com a sexo: ')).upper()
    somaidade += i
    if x == 1 and s in 'Mm':
        hvelho = i
        hvelhonome = n
    if s in 'Mm' and i > hvelho:
        hvelho = i
        hvelhonome = n
    if s in 'Ff' and i < 20:
        mnovas += 1

mediaidade = somaidade / 4
print('------------')
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O Homem mais velho do grupo tem {} anos e se chama {}.'.format(hvelho, hvelhonome.capitalize()))
print('O numero de mulheres com idade menor que 20 anos é de : {}'.format(mnovas))
print('------------')
