s = float(input('Entre com o salario do funcionario: '))
if s <= 1250.00:
    s = s + (s*(15/100))
    print('O novo salario do funcionario é: {:.2f}'.format(s))
else:
    s = s + (s*(10/100))
    print('O novo salario do funcionario é: {:.2f}'.format(s))
