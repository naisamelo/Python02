soma = 0
for c in range(1, 11):
    n = float(input('Digite o {}º valor: '.format(c)))
    soma = soma + n
media = soma/10
print('A Média das notas é {:.2f}'.format(media))

