km = float(input('Entre com a quantidade de KM percorridos pelo veiculo: '))
d = int(input('Entre com a quantidade de dias nos quais o veiculo foi alugado: '))
v = (km*0.15)+(60*d)
print('O valor total a pagar é de: R${:.2f}'.format(v))