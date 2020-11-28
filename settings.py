import pygame

class Settings():
    def __init__(self):
        self.cell_size = 20
        self.cell_number = 24
        self.screen_width = self.cell_size * self.cell_number
        self.screen_height = self.cell_size * self.cell_number
        self.bg_color = (64, 64, 64)
        self.font = pygame.font.Font("font/PixelSplitter.ttf", 16)