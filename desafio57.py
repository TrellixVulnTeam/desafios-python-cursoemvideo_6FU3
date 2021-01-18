sexo = str(input('Entre com o sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
        sexo = str(input('Digite novamente!Entre com o sexo: ').strip().upper()[0])
print('Sexo {} registrado com sucesso'.format(sexo))