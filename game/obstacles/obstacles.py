import pygame
from game.settings import HEIGHT, RED

class Obstacles:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.obstacles = [
            {"x": 200, "y": HEIGHT - self.height},
            {"x": 400, "y": HEIGHT - self.height},
            {"x": 600, "y": HEIGHT - self.height},
        ]

    def draw(self, window):
        for obstacle in self.obstacles:
            pygame.draw.rect(window, RED, (obstacle["x"], obstacle["y"], self.width, self.height))

def check_collision(player_x, player_y, player_size, obstacles):
    for obstacle in obstacles:
        if (player_x < obstacle["x"] + 50 and
            player_x + player_size > obstacle["x"] and
            player_y < obstacle["y"] + 50 and
            player_y + player_size > obstacle["y"]):
            return True
    return False
