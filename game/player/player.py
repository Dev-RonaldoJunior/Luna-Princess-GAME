import pygame
from game.settings import WIDTH, HEIGHT, BLACK
from game.platforms import check_platform_collision, check_head_collision

class Player:
    def __init__(self):
        self.size = 50
        self.x = 50
        self.y = HEIGHT - self.size
        self.speed = 5
        self.jump_height = 15
        self.is_jumping = False
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_cooldown = 0.6  # Tempo de cooldown em segundos
        self.last_jump_time = 0

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:  # Verifica se o jogador não ultrapassa o lado esquerdo da tela
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.size:  # Verifica se o jogador não ultrapassa o lado direito da tela
            self.x += self.speed

    def jump(self, keys):
        current_time = pygame.time.get_ticks() / 1000  # Tempo atual em segundos
        if not self.is_jumping and keys[pygame.K_SPACE] and current_time - self.last_jump_time > self.jump_cooldown:
            self.is_jumping = True
            self.velocity_y = -self.jump_height
            self.last_jump_time = current_time

    def update(self, platforms):
        if self.is_jumping:
            self.y += self.velocity_y
            self.velocity_y += self.gravity

            head_platform = check_head_collision(self.x, self.y, self.size, platforms)
            if head_platform and self.velocity_y < 0:
                self.y = head_platform["y"] + 20
                self.velocity_y = 0

            platform = check_platform_collision(self.x, self.y, self.size, platforms)
            if platform and self.velocity_y >= 0:
                self.y = platform["y"] - self.size
                self.is_jumping = False
                self.velocity_y = 0

            if self.y >= HEIGHT - self.size:
                self.y = HEIGHT - self.size
                self.is_jumping = False
        else:
            on_platform = check_platform_collision(self.x, self.y, self.size, platforms)
            if not on_platform and self.y < HEIGHT - self.size:
                self.is_jumping = True
                self.velocity_y = 0
            if on_platform and self.y + self.size > on_platform["y"]:
                self.y = on_platform["y"] - self.size
                self.is_jumping = False
                self.velocity_y = 0

    def draw(self, window):
        pygame.draw.rect(window, BLACK, (self.x, self.y, self.size, self.size))
