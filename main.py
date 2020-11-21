import sys
import pygame
from pygame.math import Vector2
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

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                snake.move_snake()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    snake.direction = Vector2(1, 0)

        screen.fill(settings.bg_color)

        snack.create_snack()
        snake.create_snake()

        pygame.display.update()

        clock.tick(60)

main()