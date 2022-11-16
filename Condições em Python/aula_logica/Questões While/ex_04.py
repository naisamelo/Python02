alunos = int(input('Informe o número de alunos na turma: '))
c = 1
soma = 0
while c <= alunos:
    nota = float(input('Nota do {}º aluno: '.format(c)))
    soma = soma + nota
    c = c + 1
print('Média da turma {:.2f}'.format(soma/alunos))