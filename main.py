import sys
import pygame
from pygame.math import Vector2
from settings import Settings
from objects import Snake, Snack

pygame.init()

settings = Settings()

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("Snake")

snack = Snack(screen)
snake = Snake(screen)


def check_collision():
    if snack.position == snake.body[0]:
        snack.throw()
        snake.grow()


def main():

    clock = pygame.time.Clock()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                snake.move()
                check_collision()
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

        snack.make()
        snake.hatch()

        pygame.display.update()

        clock.tick(60)

main()