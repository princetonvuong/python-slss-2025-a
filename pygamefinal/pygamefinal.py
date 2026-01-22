# Author: Princeton Vuong




import pygame
import random
from pygame import Surface

# ---------- CONSTANTS ----------
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
FLIP_FORCE = -10
OBSTACLE_SPEED = 6
GAP_SIZE = 160
size = (WIDTH, HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)

TITLE = "Gravity Dodge"

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# text function
def write_text(surface, text, x, y, size):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surface = font.render(text, True, WHITE)
    surface.blit(text_surface, (x, y))

# AI was used to help center the text
def write_text_center(surface, text, center_x, center_y, size):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surface = font.render(text, True, WHITE)
    rect = text_surface.get_rect(center=(center_x, center_y))
    surface.blit(text_surface, rect)

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/kirby.png")
        self.image = pygame.transform.scale_by(self.image, 0.03)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)

        self.velocity = 0
        self.gravity_dir = 1  # 1 = down, -1 = up

    # AI was used here to create the gravity effect, I couldnt figure out how to add it so I used AI to help write it
    def update(self):
        self.velocity += GRAVITY * self.gravity_dir
        self.rect.y += self.velocity

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity = 0

    def flip_gravity(self):
        self.gravity_dir *= -1
        self.velocity = FLIP_FORCE * self.gravity_dir

        # flip sprite
        self.image = pygame.transform.flip(self.image, False, True)


# Obstable class
class Obstacle:
    def __init__(self):
        gap_y = random.randint(100, HEIGHT - 100)

        self.top_rect = pygame.Rect(WIDTH, 0, 60, gap_y - GAP_SIZE // 2)
        self.bottom_rect = pygame.Rect(
            WIDTH,
            gap_y + GAP_SIZE // 2,
            60,
            HEIGHT - (gap_y + GAP_SIZE // 2),
        )

    def update(self):
        self.top_rect.x -= OBSTACLE_SPEED
        self.bottom_rect.x -= OBSTACLE_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.top_rect)
        pygame.draw.rect(surface, RED, self.bottom_rect)

# Taken from flappy-bird game
class Background:
    def __init__(self) -> None:
        self.image = (
            pygame.image.load('images/background.png')
            .convert()
            .subsurface(0, 0, WIDTH, HEIGHT)
        )
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.rect2 = self.image.get_rect()
        self.rect2.x = WIDTH
        self.rect2.y = 0

    def draw(self, screen: Surface) -> None:
        self.rect.x -= 1
        self.rect2.x -= 1
        if self.rect.x <= -WIDTH:
            self.rect.x = WIDTH
        elif self.rect2.x <= -WIDTH:
            self.rect2.x = WIDTH
        screen.blit(self.image, self.rect)
        screen.blit(self.image, self.rect2)


# main game
def main():
    background = Background()
    player = Player()
    player_group = pygame.sprite.Group(player)
    obstacles = []

    score = 0
    spawn_timer = 0
    game_over = False
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        # Pressing esc will leave the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    player.flip_gravity()

                if event.key == pygame.K_ESCAPE:
                    running = False

        if not game_over:
            player_group.update()

            spawn_timer += 1
            if spawn_timer > 90:
                obstacles.append(Obstacle())
                spawn_timer = 0

            for obs in obstacles:
                obs.update()
                if (
                    player.rect.colliderect(obs.top_rect)
                    or player.rect.colliderect(obs.bottom_rect)
                ):
                    game_over = True

            obstacles = [o for o in obstacles if o.top_rect.right > 0]
            score += 1


        # draw
        background.draw(screen)

        player_group.draw(screen)
        for obs in obstacles:
            obs.draw(screen)

        write_text(screen, f"Score: {score}", 10, 10, 30)

        if game_over:
            write_text_center(screen, "GAME OVER", WIDTH // 2, HEIGHT // 2 - 30, 48)
            write_text_center(screen, "Press ESC to exit", WIDTH // 2, HEIGHT // 2 + 20, 24)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
