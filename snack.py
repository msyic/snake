import pygame
import random
from pygame.math import Vector2
from settings import Settings

settings = Settings()

class Snack():
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, settings.cell_number - 1)
        self.y = random.randint(0, settings.cell_number - 1)
        self.position = Vector2(self.x, self.y)

    def create_snack(self):
        snack_rect = pygame.Rect(int(self.position.x * settings.cell_size), int(self.position.y * settings.cell_size), settings.cell_size, settings.cell_size)
        pygame.draw.rect(self.screen, (255, 0, 0), snack_rect)