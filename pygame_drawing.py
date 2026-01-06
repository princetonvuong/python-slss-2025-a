# Pygame Drawing
# Author: Ubial
# 5 January 2026

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Your Title Here")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        pygame.draw.rect(screen, RED, (300, 300, 200, 150))

        pygame.draw.rect(screen, BROWN := (139, 69, 19), (380, 360, 40, 90))

        pygame.draw.rect(screen, BLUE, (330, 330, 40, 40))
        pygame.draw.rect(screen, BLUE, (430, 330, 40, 40))

        pygame.draw.rect(screen, GREY, (290, 270, 220, 30))

        pygame.display.flip()

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
