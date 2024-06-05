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
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def main():
    # STATUS DO PERSONAGEM
    player_size = 50
    player_x = 50
    player_y = HEIGHT - player_size
    player_speed = 5
    jump_height = 15
    is_jumping = False
    velocity_y = 0
    gravity = 0.8

    # OBSTÁCULOS
    obstacle_width = 50
    obstacle_height = 50
    obstacles = [
        {"x": 200, "y": HEIGHT - obstacle_height},
        {"x": 400, "y": HEIGHT - obstacle_height},
        {"x": 600, "y": HEIGHT - obstacle_height},
    ]

    # PLATAFORMAS
    platform_width = 100
    platform_height = 20
    platforms = [
        {"x": 150, "y": HEIGHT - 150},
        {"x": 350, "y": HEIGHT - 300},
        {"x": 550, "y": HEIGHT - 450},
    ]

    # CONTROLE DE TEMPO
    clock = pygame.time.Clock()

    # FUNÇÃO DOS OBSTÁCULOS
    def check_collision(player_x, player_y, player_size, obstacles):
        for obstacle in obstacles:
            if (player_x < obstacle["x"] + obstacle_width and
                player_x + player_size > obstacle["x"] and
                player_y < obstacle["y"] + obstacle_height and
                player_y + player_size > obstacle["y"]):
                return True
        return False
    
    # FUNÇÃO DAS PLATAFORMAS
    def check_platform_collision(player_x, player_y, player_size, platforms):
        for platform in platforms:
            if (player_x < platform["x"] + platform_width and
                player_x + player_size > platform["x"] and
                player_y + player_size > platform["y"] and
                player_y < platform["y"] + platform_height):
                return platform
        return None
    
    def check_head_collision(player_x, player_y, player_size, platforms):
        for platform in platforms:
            if (player_x < platform["x"] + platform_width and
                player_x + player_size > platform["x"] and
                player_y < platform["y"] + platform_height and
                player_y > platform["y"]):
                return platform
        return None

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

            # VERIFICAR COLISÃO COM PLATAFORMAS DURANTE PULO
            head_platform = check_head_collision(player_x, player_y, player_size, platforms)
            if head_platform and velocity_y <0:
                player_y = head_platform["y"] + platform_height
                velocity_y = 0

            # VERIFICAR COLISÃO COM PLATAFORMAS DURANTE A QUEDA
            platform = check_platform_collision(player_x, player_y, player_size, platforms)
            if platform and velocity_y >= 0:
                player_y = platform["y"] - player_size
                is_jumping = False
                velocity_y = 0

            if player_y >= HEIGHT - player_size:
                player_y = HEIGHT - player_size
                is_jumping = False
        
        else:
            # VERIFICAR SE O PLAYER ESTA EM CIMA DA PLATAFORMA
            on_platform = check_platform_collision(player_x, player_y, player_size, platforms)
            if not on_platform and player_y < HEIGHT - player_size:
                is_jumping = True
                velocity_y = 0

            #IMPEDE O PLAYER DE PASSAR POR BAIXO DA PLATAFORMA
            if on_platform and player_y + player_size > on_platform["y"]:
                player_y = on_platform["y"] - player_size
                is_jumping = False
                velocity_y = 0

        # VERIFICAR COLISÃO COM OBSTÁCULOS
        if check_collision(player_x, player_y, player_size, obstacles):
            print("Colisão detectada!")
            main()  # Reinicia o jogo
            return  # Sai da função atual para evitar múltiplos jogos simultâneos

        # DESENHAR CENÁRIO
        window.fill(WHITE)

        # DESENHAR JOGADOR
        pygame.draw.rect(window, BLACK, (player_x, player_y, player_size, player_size))

        # DESENHAR OBSTÁCULOS
        for obstacle in obstacles:
            pygame.draw.rect(window, RED, (obstacle["x"], obstacle["y"], obstacle_width, obstacle_height))

        # DESENHAR PLATAFORMAS
        for platform in platforms:
            pygame.draw.rect(window, GREEN, (platform["x"], platform["y"], platform_width, platform_height))
        
        pygame.display.update()

        # CONTROLAR TAXA DE QUADROS
        clock.tick(60)

# INICIAR O JOGO
main()