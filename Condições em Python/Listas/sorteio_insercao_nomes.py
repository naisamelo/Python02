import random
# nomes = input('1 nome: '), input('2 nome: '), input('3 nome: ')
nomes = []
c = 1
while c <= 5:
    nomes.append(input('Nome do aluno: '))
    c = c + 1

print('Os alunos sorteado é: {}'.format(random.choice(nomes)))


