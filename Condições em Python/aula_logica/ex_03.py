func = str(input('Nome do Funcionário: '))
sal = float(input('Salário: '))
if sal >= 2.000 and sal <= 3.000:
    aumento = sal + (sal * 15 / 100)
elif sal > 3.000:
    aumento = sal + (sal * 5 / 100)
elif sal < 2.000:
    aumento = sal + (sal * 25 / 100)
print('O {} ganhava {} e passou a receber {}'.format(func, sal, aumento))