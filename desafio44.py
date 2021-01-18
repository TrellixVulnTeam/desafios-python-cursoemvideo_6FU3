preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[1] A VISTA
[2] A VISTA NO CARTAO
[3] 2X NO CARTAO
[4] 3X OU MAIS NO CARTAO''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
elif opcao == 4:
    total = preco
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = total
    print('Opcao invaliida. Tente novamente.')
print('Sua compra de {:.2f} vai custar R${:.2f} no final.'.format(preco, total))
