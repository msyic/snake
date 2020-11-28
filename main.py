import sys
import pygame
from pygame.math import Vector2
from settings import Settings
from objects import Snake, Snack
from stats import Score

pygame.init()

settings = Settings()

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("Snake")

snack = Snack(settings, screen)
snake = Snake(settings, screen)
score = Score(settings, screen, snake)


def check_collision():
    if snack.position == snake.body[0]:
        snack.throw()
        snake.grow()

    for block in snake.body[1:]:
        if block == snack.position:
            snack.throw()

def check_fail():
    if (not 0 <= snake.body[0].x < settings.cell_number) or (not 0 <= snake.body[0].y < settings.cell_number):
        game_over()

    for block in snake.body[1:]:
        if block == snake.body[0]:
            game_over()

def game_over():
    pygame.quit()
    sys.exit()



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
            check_fail()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake.direction.y != 1:
                    snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if snake.direction.y != -1:
                    snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if snake.direction.x != 1:
                    snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if snake.direction.x != -1:
                    snake.direction = Vector2(1, 0)

    screen.fill(settings.bg_color)

    snack.make()
    snake.hatch()
    score.draw()

    pygame.display.update()

    clock.tick(60)