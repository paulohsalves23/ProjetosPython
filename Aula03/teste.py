import random

def play():
    print(25*"/")
    print("/   O Jogo da Forca     / ")
    print(25*"/","\n")

    # Metodo implementado para gerar um pais presenta na lista de forma randomica
    pais_secreto = ['brasil', 'australia', 'japao', 'canada', 'gana', 'grecia','peru', 'china', 'chile', 'cuba', 'belgica', 'polonia', 'jamaica', 'paraguai', 'alemanha', 'zimbabue', 'argentina', 'dinamarca', 'madagascar', 'eslovaquia', 'montenegro']
    random.shuffle(pais_secreto)
    pais_secreto = (pais_secreto[0]).upper()
    letras_acertadas = ("_" * len(pais_secreto))
    print(letras_acertadas)
    letras_certas = (list(letras_acertadas))
    print(letras_certas)

    enforcou = False
    escapou = False
    tentativas = 1

    print(pais_secreto)


    while(not enforcou and not escapou):
        print(f"O país tem {len(pais_secreto)} letras.", "\n")

        chute = input("chute uma letra: ")
        chute = chute.strip().upper()

        # Logica de chutes, quando errado sobe uma tentativa, ao acertar não sobe
        if chute not in pais_secreto:
            tentativas += 1
            print(f"Você ainda tem {len(pais_secreto) - tentativas + 1} para jogar")
        else:
            posicao =  0
            for letra in pais_secreto:
                if(chute == letra):
                    letras_certas[posicao] = letra
                posicao += 1

        # Metodo para quantidade de tentativas ser do tamanho do pais secreto
        enforcou = tentativas > len(pais_secreto)
        if(enforcou == True):
            print("Você se enforcou")
        print(letras_certas)

        # Metodo para transformar a lista em uma string e finalizar o jogo quando o pais for completo
        acertou = ''.join(letras_certas)
        if(acertou == pais_secreto):
            print("\n", "Parabéns, você escapou da forca!")
            break


if(__name__ == "__main__"):
    play()