import random

def realizar_sorteio(nomes):
    print("Realizando sorteio...")
    while nomes:
        sorteado = random.choice(nomes)
        nomes.remove(sorteado)
    
    print(f"O sorteado é: {sorteado}")
    print("Sorteio concluído!")

lista_de_nomes = ["Ilos", "Vicente", "Naisa", "Edimar", "Edilmara", "Adriano", "Ketrin"]
realizar_sorteio(lista_de_nomes)