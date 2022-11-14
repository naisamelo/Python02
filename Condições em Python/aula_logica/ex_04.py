casa = float(input('Qual o valor da casa: R$ '))
sal = float(input('Qual salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12) #Divide o valor da casa em meses
minino = sal * 30 / 100 #Retorna 30% do valor do salário
print('Para pagar uma casa de R${:.2f} em anos {}'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minino:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')