n1 = float(input('Entre com o primeiro valor: '))
n2 = float(input('Entre com o segundo valor: '))
opcao = 0
while opcao != 5:
    print('-----------------------------------------')
    print('MENU: [1]SOMAR; [2]MULTIPLICAR; [3]MAIOR; [4]NOVOS NÚMEROS; [5]SAIR DO PROGRAMA')
    opcao = int(input('Entre com uma das opções do MENU: '))
    print('-----------------------------------------')

if opcao == 1:
   result = n1 + n2
   print('O resultado da soma de {} e {} é : {}'.format(n1, n2, result))
elif opcao == 2:
   result = n1 * n2
   print('O resultado da multiplicacao de {} e {} é : {}'.format(n1, n2, result))
elif opcao == 3:
    if n1 > n2:
        result = n1
        print('{} é MAIOR que {}.'.format(n1, n2))
    else:
        result = n2
        print('{} é MAIOR que {}.'.format(n2, n1))
elif opcao == 4:
    print('Informe os numeros novamente:')
    n1 = float(input('Entre com o primeiro valor: '))
    n2 = float(input('Entre com o segundo valor: '))
elif opcao == 5:
    print('Finalizando')
else:
    print('Opção Invalida.')
print('-----------------------------------------')