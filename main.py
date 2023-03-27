import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Set up the window for the game.
screen = pygame.display.set_mode([500, 500])

#Set up the game loop.
running = True
while running:

    # If the user click on the close button it ends.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    
    #update the screen.
    pygame.display.flip()

#Game loop ends.
pygame.quit()