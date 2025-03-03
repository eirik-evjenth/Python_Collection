import pygame
import random

# Initialiser Pygame
pygame.init()

# Skjermstørrelse og tittel
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plastic Cleanup")

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60
# Skalering
SCALE = 1.2

# Last inn bilder
crab_image = pygame.image.load("crab.png")
crab_image = pygame.transform.scale(crab_image, (int(75 * SCALE), int(75 * SCALE)))
plastic_image = pygame.image.load("trash.png")
plastic_image = pygame.transform.scale(plastic_image, (int(75 * SCALE), int(75 * SCALE)))

# Spillerklasse
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - int(70 * SCALE), int(75 * SCALE), int(70 * SCALE))
        self.speed = int(5 * SCALE)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(crab_image, (self.rect.x, self.rect.y))
        # Uncomment the following line to draw the hitbox
        # pygame.draw.rect(screen, WHITE, self.rect, 2)

# Hindringklasse
class Obstacle:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 60), -60, 58, 50)
        self.hitbox = self.rect.copy()
        self.hitbox.x += 8  # Shift hitbox to the right by 10 units
        self.hitbox.y += 10
        self.speed = random.randint(3, 6)

    def move(self):
        self.rect.y += self.speed
        self.hitbox.y += self.speed

    def draw(self, screen):
        screen.blit(plastic_image, (self.rect.x, self.rect.y))
        # Uncomment the following line to draw the hitbox
        # pygame.draw.rect(screen, WHITE, self.hitbox, 2)

# Tegn bakgrunn
def draw_background(screen):
    # Draw blue background
    screen.fill((0, 191, 255))  # Deep sky blue color

    # Draw sand at the bottom
    pygame.draw.rect(screen, (194, 178, 128), (0, HEIGHT - 100, WIDTH, 100))  # Sand color

# Hovedspillfunksjon
def main():
    run = True
    player = Player()
    obstacles = []
    spawn_timer = 0
    score = 0
    quickness = 0

    font = pygame.font.SysFont(None, 36)

    while run:
        draw_background(screen)  # Draw the new background

        # Håndter hendelser
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Oppdater spiller
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Generer hindringer
        spawn_timer += 1
        if spawn_timer > 30 - quickness:  # Hver 30 frames
            obstacles.append(Obstacle())
            spawn_timer = 0
            if not quickness > 20:
                quickness += 0.5

        # Oppdater hindringer
        for obstacle in obstacles[:]:
            obstacle.move()
            if obstacle.rect.top > HEIGHT:
                obstacles.remove(obstacle)
                score += 1

            if player.rect.colliderect(obstacle.rect):
                run = False

        # Tegn alt
        player.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        # Tegn score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
