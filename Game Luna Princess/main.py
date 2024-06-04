import pygame
import sys

# INICIANDO O PYGAME
pygame.init()

# CONFIGURAÇÕES DA TELA
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Luna Princess')

# DEFININDO CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# STATUS DO PERSONAGEM
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 5
jump_height = 15
is_jumping = False
velocity_y = 0
gravity = 0.8

# LOOP PRINCIPAL DO JOGO
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # MOVIMENTAÇÃO DO PERSONAGEM
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # LIMITANDO O MOVIMENTO DENTRO DA JANELA
    if player_x < 0:
        player_x = 0
    elif player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    # SALTO DO PERSONAGEM    
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            velocity_y = -jump_height

    if is_jumping:
        player_y += velocity_y
        velocity_y += gravity
        if player_y >= HEIGHT - player_size:
            player_y = HEIGHT - player_size
            is_jumping = False

    # DESENHAR NA TELA
    window.fill(WHITE)
    pygame.draw.rect(window, BLACK, (player_x, player_y, player_size, player_size))
    pygame.display.update()

    pygame.time.delay(30)
    