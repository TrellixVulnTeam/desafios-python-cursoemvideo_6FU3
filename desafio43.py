peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Voce esta na faixa de peso normal')
elif 25 <= imc < 30:
    print('Voce esta em sobrepeso')
elif 30 <= imc < 40:
    print('Voce esta em obesidade')
elif imc >= 40:
    print('Voce esta em obesidade morbida')