import random

def realizar_sorteio(nomes):
    print("Realizando sorteio...")
    while nomes:
        sorteado = random.choice(nomes)
        nomes.remove(sorteado)
    
    print(f"O sorteado é: {sorteado}")
    print("Sorteio concluído!")

alunos = []
c = 1
while c <= 5:
    alunos.append(input('Nome do aluno: '))
    c = c + 1

realizar_sorteio(alunos)