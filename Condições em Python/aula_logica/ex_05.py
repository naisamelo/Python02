peso = float(input('Digite seu peso (Kg) '))
altura = float(input('Digite sua altura (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso Ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obsidade Mórbida')