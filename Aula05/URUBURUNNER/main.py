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

# Importa a fonte
fonte_titulo = pygame.font.Font('assets/fontes/LeafCrownDemoRegular.ttf', 150)
fonte_menu = pygame.font.Font('assets/fontes/LeafCrownDemoOutline.ttf', 80)

# Importa as telas de fundo
fundos7 = pygame.image.load('assets/planoFundo/fireflys.png') # Carrega a imagem do fundo
fundos5 = pygame.image.load('assets/planoFundo/grass&road.png') # Carrega a imagem do fundo
fundos4 = pygame.image.load('assets/planoFundo/grasses.png') # Carrega a imagem do fundo
fundos2 = pygame.image.load('assets/planoFundo/jungle_bg.png') # Carrega a imagem do fundo
fundos6 = pygame.image.load('assets/planoFundo/lianas.png') # Carrega a imagem do fundo
fundos1 = pygame.image.load('assets/planoFundo/sky.png') # Carrega a imagem do fundo
fundos8 = pygame.image.load('assets/planoFundo/tree_face.png') # Carrega a imagem do fundo
fundos3 = pygame.image.load('assets/planoFundo/trees&bushes.png') # Carrega a imagem do fundo

# Redimensiona as imagens do plano de fundo
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
index_urubu1 = 0 # Índice para controlar a animação do urubu

superficies_urubu = [] # Lista para armazenar as imagens do urubu
superficies_urubu1 = [] # Lista para armazenar as imagens do urubu
animaVooReverso = False

# Carrega as imagens do urubu parado
for imagem in range(5):
    urubu_superficie = pygame.image.load(f"assets/parado/tile00{imagem}.png") # Carrega a imagem do urubu
    superficies_urubu.append(urubu_superficie)

# Carrega as imagens do urubu
for imagem1 in range(5, 10):
    urubu_superficie1 = pygame.image.load(f"assets/pulo/tile00{imagem1}.png") # Carrega a imagem do urubu voando
    # Rotaciona em 35 graus a imagem do urubu
    #urubu_voando_superficie = pygame.transform.rotate(urubu_voando_superficie, -35)
        
    superficies_urubu1.append(urubu_superficie1)

# Cria o retângulo do urubu a partir da lista de imagens
urubu_retangulo = superficies_urubu[index_urubu].get_rect(center = (100, 350)) # Cria o retangulo do urubu
urubu_retangulo1 = superficies_urubu1[index_urubu1].get_rect(center = (150, 250)) # Cria o retangulo do urubu

# Textos do Menu
titulo = fonte_titulo.render("FlappyBu", True, (255, 255, 255)) # Renderiza o texto do título
menu_jogar = fonte_menu.render("Aperte Espaço para Jogar", True, (255, 255, 255)) # Renderiza o texto do menu

# Loop do jogo
jogo_comecou = False

# Gravidade do urubu
gravidade = 1

while True:
    # Checa os eventos do jogo
    for evento in pygame.event.get():
        print(evento)

        if evento.type == pygame.QUIT:
            # Fecha a janela
            pygame.quit()

            # Fecha o jogo
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogo_comecou = True
                ativaAnimacao = True
                gravidade = -30

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

    if not jogo_comecou:
            # Desenha o título na tela na posição central usando o tamanho da tela e a largura do texto
            tela.blit(titulo, (tamanho_tela[0] / 2 - titulo.get_width() / 2, 50))
            # Desenha o menu na tela
            tela.blit(menu_jogar, (tamanho_tela[0] / 2 - menu_jogar.get_width() / 2, 230))

            # Desenha o urubu na tela
            tela.blit(superficies_urubu[int(index_urubu)], urubu_retangulo)
            # Atualiza o índice do urubu para animar
            index_urubu += 0.15
            # Checa se o índice do urubu é maior que o tamanho da lista de imagens
            if index_urubu >= len(superficies_urubu):
                index_urubu = 0

    else: 

            # Atualiza o índice do urubu para animar
        if ativaAnimacao:
            if animaVooReverso:
                index_urubu1 -= 1.2
            else:
                index_urubu1 += 1.2

        # Aumenta a gravidade
        gravidade += 3

        # Adiciona a gravidade ao urubu
        urubu_retangulo1.y += gravidade

        # Desenha o urubu na tela voando
        tela.blit(superficies_urubu1[int(index_urubu1)], urubu_retangulo1)

         # Checa se o índice do urubu é maior que o tamanho da lista de imagens
    if index_urubu1 >= len(superficies_urubu1) - 1:
        animaVooReverso = True
    elif index_urubu1 <= 0:
        animaVooReverso = False

    # Atualiza a tela para mostrar as mudanças
    pygame.display.update()

    # Controla o FPS em 60 frames por segundo
    relogio.tick(60)