import sys
import pygame

def run():
    pygame.init()   # Initialize pygame.

    screen_width = 500
    screen_height = 500
    bg_color = (255, 255, 255)
    
    screen = pygame.display.set_mode((screen_width, screen_height)) # Create a window.
    pygame.display.set_caption("Snake")

    while True:
        for event in pygame.event.get():    # Look for a user action.
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)   # Fill the background.
        
        pygame.display.flip()   # Update the screen.

run()