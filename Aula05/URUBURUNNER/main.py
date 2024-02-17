import pygame

# Inicialia a biblioteca do pygame
pygame.init()

# Criar uma tela
tamanho_tela = (960, 540)
tela = pygame.display.set_mode((tamanho_tela))

# Cria um relógio para controlar o FPS
relogio = pygame.time.Clock()

# Título da tela
pygame.display.set_caption("Urubu Runner")

# Importa as telas de fundo
fundos7 = pygame.image.load('assets/planoFundo/fireflys.png') # Carrega a imagem do fundo
fundos5 = pygame.image.load('assets/planoFundo/grass&road.png') # Carrega a imagem do fundo
fundos4 = pygame.image.load('assets/planoFundo/grasses.png') # Carrega a imagem do fundo
fundos2 = pygame.image.load('assets/planoFundo/jungle_bg.png') # Carrega a imagem do fundo
fundos6 = pygame.image.load('assets/planoFundo/lianas.png') # Carrega a imagem do fundo
fundos1 = pygame.image.load('assets/planoFundo/sky.png') # Carrega a imagem do fundo
fundos8 = pygame.image.load('assets/planoFundo/tree_face.png') # Carrega a imagem do fundo
fundos3 = pygame.image.load('assets/planoFundo/trees&bushes.png') # Carrega a imagem do fundo

fundos1 = pygame.transform.scale(fundos1, tamanho_tela)
fundos2 = pygame.transform.scale(fundos2, tamanho_tela)
fundos3 = pygame.transform.scale(fundos3, tamanho_tela)
fundos4 = pygame.transform.scale(fundos4, tamanho_tela)
fundos5 = pygame.transform.scale(fundos5, tamanho_tela)
fundos6 = pygame.transform.scale(fundos6, tamanho_tela)
fundos7 = pygame.transform.scale(fundos7, tamanho_tela)
fundos8 = pygame.transform.scale(fundos8, tamanho_tela)

# Jogador Urubu
index_urubu = 0 # Índice para controlar a animação do urubu
superficies_urubu = [] # Lista para armazenar as imagens do urubu

# Carrega as imagens do urubu
for imagem in range(5):
    urubu_superficie = pygame.image.load(f"assets/parado/tile00{imagem}.png") # Carrega a imagem do urubu
    superficies_urubu.append(urubu_superficie)

# Cria o retângulo do urubu a partir da lista de imagens
urubu_retangulo = superficies_urubu[index_urubu].get_rect(center = (100, 350)) # Cria o retangulo do urubu

# Loop do jogo
while True:
    # Checa os eventos do jogo
    for evento in pygame.event.get():
        print(evento)

        if evento.type == pygame.QUIT:
            # Fecha a janela
            pygame.quit()

            # Fecha o jogo
            exit()

    # Preenche a tela com a cor laranja
    tela.fill((205, 92, 92))

    # Desenha os fundos da tela
    tela.blit(fundos1, (0, 0))
    tela.blit(fundos2, (0, 0))
    tela.blit(fundos3, (0, 0))
    tela.blit(fundos4, (0, 0))
    tela.blit(fundos5, (0, 0))
    tela.blit(fundos6, (0, 0))
    tela.blit(fundos7, (0, 0))
    tela.blit(fundos8, (0, 0))

    # Desenha o urubu na tela
    tela.blit(superficies_urubu[int(index_urubu)], urubu_retangulo)

    # Atualiza o índice do urubu para animar
    index_urubu += 0.15

    # Checa se o índice do urubu é maior que o tamanho da lista de imagens
    if index_urubu >= len(superficies_urubu):
        index_urubu = 0

    # Atualiza a tela para mostrar as mudanças
    pygame.display.update()

    # Controla o FPS em 60 frames por segundo
    relogio.tick(60)