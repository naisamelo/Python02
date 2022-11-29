maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Peso {c}'))
    if peso > 0:
        peso = maior
        peso = menor
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'maior {maior} menor {menor}')