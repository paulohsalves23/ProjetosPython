nome = (input("Qual seu nome?"))

altura = float(input("Fale sua altura em metros:"))
peso = float(input("Agora informe seu peso em Kg:"))

print(f"{nome},seu IMC (índice de massa corpórea) é {peso / (altura*altura)}")