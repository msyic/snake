import pygame
from pygame.math import Vector2
from settings import Settings

settings = Settings()

class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def create_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * settings.cell_size), int(block.y * settings.cell_size), settings.cell_size - 2, settings.cell_size - 2)
            pygame.draw.rect(self.screen, (0, 255, 0), block_rect)