import sys
import pygame
from settings import Settings
from snack import Snack
from snake import Snake

def main():
    pygame.init()

    settings = Settings()
    
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()

    snack = Snack(screen)
    snake = Snake(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(settings.bg_color)

        snack.create_snack()
        snake.create_snake()

        pygame.display.update()

        clock.tick(60)

main()