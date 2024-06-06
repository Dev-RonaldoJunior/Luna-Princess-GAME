import pygame
from game.settings import HEIGHT, GREEN

class Platforms:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.platforms = [
            {"x": 150, "y": HEIGHT - 150},
            {"x": 350, "y": HEIGHT - 300},
            {"x": 550, "y": HEIGHT - 450},
        ]

    def draw(self, window):
        for platform in self.platforms:
            pygame.draw.rect(window, GREEN, (platform["x"], platform["y"], self.width, self.height))

def check_platform_collision(player_x, player_y, player_size, platforms):
    for platform in platforms:
        if (player_x < platform["x"] + 100 and
            player_x + player_size > platform["x"] and
            player_y + player_size > platform["y"] and
            player_y < platform["y"] + 20):
            return platform
    return None

def check_head_collision(player_x, player_y, player_size, platforms):
    for platform in platforms:
        if (player_x < platform["x"] + 100 and
            player_x + player_size > platform["x"] and
            player_y < platform["y"] + 20 and
            player_y > platform["y"]):
            return platform
    return None
