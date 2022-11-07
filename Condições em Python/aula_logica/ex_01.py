nome = str(input('Nome do aluno(a): '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
média = (n1 + n2)/2
if média >= 6:
    print('Aluno(a): {}'.format(nome))
    print('Média: {:.2f}'.format(média))
    print('Situação: Aprovado!')
else:
    print('''Aluno(a): {}
    'Média: {:.2f}'
    'Situação: Reprovado!'''.format(nome, média))
