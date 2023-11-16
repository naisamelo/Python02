n = int(input("Digite um número para ver a tabuada: "))
if 1 < n > 10:
    print("Número Inválido! Digite novamente")
    n = int(input("Digite novamente"))
else:
    for c in range(1, 11):
        print("{} x {} = {}".format(n, c, n*c))

# Procedimento para desenhar um quadrado
def DesenharQuadrado():
    for _ in range(4):
        # Código para desenhar um lado do quadrado
        print("* ", end="")
    print()  # Muda para a próxima linha após desenhar o quadrado

# Chamando o procedimento para desenhar um quadrado
DesenharQuadrado()

