alunos = int(input('Informe a quantidade de alunos da turma:'))
c = 1
soma = 0
while c <= alunos:
    nota = float(input(f'Digite a {c}º nota: '))
    soma = soma + nota
    c = c + 1
    media = soma/alunos
print(f'A média da turma é: {media:.2f}')
