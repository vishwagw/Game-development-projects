# The main program that runs the game. 
import pygame
import sys
from player import Player
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Main game loop
def main():
    clock = pygame.time.Clock()
    player = Player()
    enemies = [Enemy() for _ in range(5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update game objects
        player.update()
        for enemy in enemies:
            enemy.update()

        # Draw everything
        screen.fill((0, 0, 0))
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
