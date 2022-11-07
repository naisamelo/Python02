nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2)/2
if média >= 6:
    print('''
    Aluno(a): {}
    Média: {:.2f}
    Situação: Aprovado!
    '''.format(nome, média))
else:
    print('''
    Aluno(a) {}
    Média: {:.2f}
    Situação: Reprovado!'''.format(nome, média))