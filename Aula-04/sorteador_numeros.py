import random

# Define a quantidade de chances
tentativas = 3

# Sorteia um número entre 1 e 50
numero_sorteado = random.randint(1, 50)

# Repete o laço enquanto houver tentativas
while tentativas > 0:
    # Pede um palpite ao usuário
    palpite = int(input("Qual o seu palpite? \n"))

    # Verifica se o palpite é igual ao número sorteado
    if palpite == numero_sorteado:
        print("Parabéns, você acertou!")
        break
    else:
        # Verifica se o palpite é maior ou menor que o número sorteado
        if palpite > numero_sorteado:
            print("Seu palpite é MAIOR")
        else:
            print("Seu palpite é MENOR")

    # Diminui a quantidade de tentativas
    tentativas -= 1

print(f"O número sorteado foi: {numero_sorteado}")
print("Você perdeu!")
print("Fim do jogo!")