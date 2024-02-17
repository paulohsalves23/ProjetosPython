import random

lista = ["Paulo","Satélite","Caracol","Nabucodonozor"]
item_aleatorio = random.choice(lista)
chances = 8

print("Bem vindo ao jogo da forca")
print()
print("Vamos tentar adivinhar uma palavra de:")
print(len(item_aleatorio))
print()

palavra = (item_aleatorio)