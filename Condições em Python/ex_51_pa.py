primeiro = int(input('Digite o termo da PA: '))
razão = int(input('Digite a razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU')
