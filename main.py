import sys
import pygame

def run():
    pygame.init()

    screen_width = 500
    screen_height = 500
    bg_color = (255, 255, 255)
    
    # Create a window on the screen.
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Snake")

    while True:

        # Wait for a key to be pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Update the screen
        pygame.display.flip()

run()