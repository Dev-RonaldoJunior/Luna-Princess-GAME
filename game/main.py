import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from game import WIDTH, HEIGHT, WHITE, Player, Obstacles, Platforms, check_collision

# INICIANDO O PYGAME
print("Iniciando Pygame")
pygame.init()

# CONFIGURAÇÕES DA TELA
print("Configurando a tela")
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Luna Princess')

# CONTROLE DE TEMPO
clock = pygame.time.Clock()

def main():
    print("Inicializando os objetos do jogo")
    player = Player()
    obstacles = Obstacles()
    platforms = Platforms()

    running = True
    game_over = False
    print("Entrando no loop principal do jogo")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Encerrando o Pygame")
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    main()  # Reinicia o jogo
                    return

        if not game_over:
            # MOVIMENTAÇÃO DO PERSONAGEM
            keys = pygame.key.get_pressed()
            player.move(keys)
            player.jump(keys)
            player.update(platforms.platforms)

            # VERIFICAR COLISÃO COM OBSTÁCULOS
            if check_collision(player.x, player.y, player.size, obstacles.obstacles):
                print("Colisão detectada!")
                game_over = True

            # DESENHAR CENÁRIO
            window.fill(WHITE)

            # DESENHAR JOGADOR
            player.draw(window)

            # DESENHAR OBSTÁCULOS
            obstacles.draw(window)

            # DESENHAR PLATAFORMAS
            platforms.draw(window)
        
        if game_over:
            font = pygame.font.SysFont(None, 55)
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            restart_text = font.render("Press Enter to Restart", True, (255, 0, 0))

            # Centralizando o texto
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))

            window.blit(game_over_text, game_over_rect)
            window.blit(restart_text, restart_rect)

        pygame.display.update()

        # CONTROLAR TAXA DE QUADROS
        clock.tick(60)
        print("Frame atualizado")

# INICIAR O JOGO
if __name__ == "__main__":
    print("Iniciando o jogo")
    main()

print("Pressione Enter para sair...")
input()
