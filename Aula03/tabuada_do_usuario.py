#Solicitar a tabuada para o usuário
multiplicador = int(input ("Informe qual multiplicador você deseja: "))

contador = 0
print(f"Essa é a Tabuada do {multiplicador}:")

while (contador <= 10):
    print(f"{multiplicador} x {contador} = {contador * multiplicador}")
    contador += 1