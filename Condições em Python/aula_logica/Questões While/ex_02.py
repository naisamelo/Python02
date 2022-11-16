i = 1
qtd_alunos = int(input('Digite a quantidade de alunos: '))
while i <= qtd_alunos:
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1 + n2)/2
    print('Media do {}º aluno: {:.2f}'.format(i,media))
    i = i + 1 