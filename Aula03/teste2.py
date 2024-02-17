import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'jogo', 'desenvolvimento']
    return random.choice(palavras)

def jogar_forca(palavra):
    letras_erradas = ''
    letras_certas = ''
    tentativas = 6
    
    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_certas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'
        
        print("Palavra: ", palavra_escondida)
        print("Letras erradas: ", letras_erradas)
        
        if palavra_escondida == palavra:
            print("Parabéns! Você venceu!")
            break
        
        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break
        
        tentativa = input("Digite uma letra: ").lower()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
        
        if tentativa in letras_erradas or tentativa in letras_certas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if tentativa in palavra:
            letras_certas += tentativa
        else:
            letras_erradas += tentativa
            tentativas -= 1

print("Bem-vindo ao jogo da forca!")
palavra = escolher_palavra()
jogar_forca(palavra)