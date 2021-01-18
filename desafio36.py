v = float(input('Entre com o valor da casa: '))
s = float(input('Entre com o salário: '))
a = int(input('Em quantos anos deseja pagar: '))

p = v/(a * 12)
m = s * 30/100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(v, a), end='')
print('a prestação será de R${:.2f}'.format(p))
if p <= m:
    print('O emprestimo pode ser concedido')
else:
    print('Emprestimo negado')


