import pygame

class Score():
    def __init__(self, settings, screen, snake):
        self.settings = settings
        self.screen = screen
        self.snake = snake

    def draw(self):
        score_text = "SCORE: " + str(len(self.snake.body) - 3)
        score_surface = self.settings.font.render(score_text, False, (255, 255, 255))
        score_x = 10
        score_y = 10
        score_rect = score_surface.get_rect(topleft = (score_x, score_y))
        self.screen.blit(score_surface, score_rect)