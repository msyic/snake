import pygame
import random
from pygame.math import Vector2
from settings import Settings


settings = Settings()


class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def hatch(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * settings.cell_size), int(block.y * settings.cell_size), settings.cell_size - 2, settings.cell_size - 2)
            pygame.draw.rect(self.screen, (0, 255, 0), block_rect)

    def move(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:    
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def grow(self):
        self.new_block = True


class Snack():
    def __init__(self, screen):
        self.screen = screen
        self.throw()

    def make(self):
        snack_rect = pygame.Rect(int(self.position.x * settings.cell_size), int(self.position.y * settings.cell_size), settings.cell_size - 2, settings.cell_size - 2)
        pygame.draw.rect(self.screen, (255, 0, 0), snack_rect)

    def throw(self):
        self.x = random.randint(0, settings.cell_number - 1)
        self.y = random.randint(0, settings.cell_number - 1)
        self.position = Vector2(self.x, self.y)