import pygame as pg
from pygame.locals import (K_w, K_a, K_s, K_d, MOUSEBUTTONDOWN)
import sys

# Initialize pygame
pg.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pg.display.set_mode([WIDTH, HEIGHT])

# Basic Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Shooter:
    def __init__(self, x, y, size, gun):
        self.rect = pg.Rect(x, y, size, size)
        self.color = WHITE
        self.speed = 5
        self.gun = gun
        self.radius = size // 2
        self.clock = pg.time.Clock()
        self.timer = pg.time.get_ticks()

    def move(self):
        """Method to move the player"""
        keys = pg.key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pg.Rect(x, y, 10, 10)
        self.color = WHITE
        self.speed = 10
        self.direction = direction

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

class Gun:
    def __init__(self, mag_size, bullets, damage):
        self.mag_size = mag_size
        self.bullets = bullets
        self.damage = damage

class Enemy:
    def __init__(self, health):
        self.health = health
        self.rect = pg.Rect(470, 300, 200, 200)

class BossAttack:
    def __init__(self, x, y, direction, speed):
        self.rect = pg.Rect(x, y, 20, 20)
        self.color = (255, 0, 0)
        self.direction = direction
        self.speed = speed

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

# Initialize objects
enemy = Enemy(500)
pistol = Gun(12, 12, 3)
player = Shooter(30, 500, 50, pistol)
bullets = []
total_health = enemy.health

# Player health
player_health = 100
player_total_health = player_health

# Boss attacks
boss_attacks = []

def boss_attack_pattern():
    """Generate boss attack patterns based on enemy health"""
    current_time = pg.time.get_ticks()
    attack_speed = max(5, 15 - (total_health - enemy.health) // 100)  # Increase speed as health decreases
    if enemy.health > 100:
        # Simple attack patterns
        if current_time % 1000 < 50:
            direction = pg.math.Vector2(1, 0).rotate(current_time % 360)
            boss_attacks.append(BossAttack(enemy.rect.centerx, enemy.rect.centery, direction, attack_speed))
        if current_time % 1500 < 50:
            direction = pg.math.Vector2(1, 0).rotate(current_time % 360)
            boss_attacks.append(BossAttack(enemy.rect.centerx, enemy.rect.centery, direction, attack_speed + 2))
        if current_time % 2000 < 50:
            direction = pg.math.Vector2(1, 0).rotate(current_time % 360)
            boss_attacks.append(BossAttack(enemy.rect.centerx, enemy.rect.centery, direction, attack_speed + 5))
    else:
        # Difficult attack pattern
        if current_time % 500 < 50:
            for angle in range(0, 360, 45):
                direction = pg.math.Vector2(1, 0).rotate(angle + (current_time // 50) % 360)  # Rotate slightly each time
                boss_attacks.append(BossAttack(enemy.rect.centerx, enemy.rect.centery, direction, attack_speed + 7))

def fade_to_black(screen, text):
    fade_surface = pg.Surface((WIDTH, HEIGHT))
    fade_surface.fill(BLACK)
    alpha = 0
    while alpha < 255:
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pg.display.flip()
        alpha += 5
        pg.time.delay(50)



def select_difficulty():
    screen.fill(BLACK)
    font = pg.font.Font(None, 72)
    difficulties = ["Easy", "Medium", "Hard"]
    selected_index = 0

    while True:
        screen.fill(BLACK)
        for i, difficulty in enumerate(difficulties):
            color = GREEN if i == selected_index else WHITE
            text = font.render(difficulty, True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100 + i * 100))
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if selected_index == 0:
                        return 5
                    elif selected_index == 1:
                        return 3
                    elif selected_index == 2:
                        return 1
                elif event.key == pg.K_UP:
                    selected_index = (selected_index - 1) % len(difficulties)
                elif event.key == pg.K_DOWN:
                    selected_index = (selected_index + 1) % len(difficulties)


def show_start_screen():
    screen.fill(BLACK)
    font = pg.font.Font(None, 72)
    options = ["Play Game", "Controls"]
    selected_index = 0

    while True:
        screen.fill(BLACK)
        for i, option in enumerate(options):
            color = GREEN if i == selected_index else WHITE
            text = font.render(option, True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100 + i * 100))
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if selected_index == 0:
                        return "play"
                    elif selected_index == 1:
                        show_controls_screen()
                elif event.key == pg.K_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pg.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)

def show_controls_screen():
    screen.fill(BLACK)
    font = pg.font.Font(None, 36)
    controls = [
        "W - Move Up",
        "A - Move Left",
        "S - Move Down",
        "D - Move Right",
        "Mouse Click - Shoot",
        "Press any key to return"
    ]

    while True:
        screen.fill(BLACK)
        for i, control in enumerate(controls):
            text = font.render(control, True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 150 + i * 50))
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                return


def show_loss_screen():
    screen.fill(BLACK)
    font = pg.font.Font(None, 72)
    options = ["Continue", "Exit"]
    selected_index = 0

    while True:
        screen.fill(BLACK)
        for i, option in enumerate(options):
            color = GREEN if i == selected_index else WHITE
            text = font.render(option, True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100 + i * 100))
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if selected_index == 1:
                        exit(1)
                    elif selected_index == 0:
                        global player_health
                        player_health += 1
                        return action == "play"
                elif event.key == pg.K_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pg.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)


# Start screen
action = show_start_screen()


# Select difficulty
player_total_health = select_difficulty()
player_health = player_total_health


# Show start screen
while True:
    if action == "play":
        # Reset game state
        enemy.health = total_health
        player_health = player_total_health
        player.gun.bullets = player.gun.mag_size
        bullets.clear()
        boss_attacks.clear()


        # Game loop
        running = True
        while running:
            # Check for events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if player.gun.bullets > 0:
                        player.gun.bullets -= 1
                        mouse_x, mouse_y = event.pos
                        direction = pg.math.Vector2(mouse_x - player.rect.centerx, mouse_y - player.rect.centery).normalize()
                        bullet = Bullet(player.rect.centerx, player.rect.centery, direction)
                        bullets.append(bullet)
                    else:
                        if pg.time.get_ticks() - player.timer >= 3500:  # Wait 3.5 seconds before reloading
                            player.timer = pg.time.get_ticks()
                            player.gun.bullets = player.gun.mag_size


            # Load background image
            background_image = pg.image.load("Background.webp", "webp")

            # Draw the background image
            screen.blit(background_image, ((WIDTH - background_image.get_width()) // 2, (HEIGHT - background_image.get_height()) // 2))


            # screen.fill(BLACK)

            # Draw the HUD box
            hud_box_width = 310
            hud_box_height = 100
            hud_box_x = 10
            hud_box_y = 10
            pg.draw.rect(screen, (50, 50, 50), (hud_box_x, hud_box_y, hud_box_width, hud_box_height))
            pg.draw.rect(screen, WHITE, (hud_box_x, hud_box_y, hud_box_width, hud_box_height), 2)

            # Draw the magazine
            mag_rect_width = 200
            mag_rect_height = 30
            mag_rect_x = hud_box_x + 20
            mag_rect_y = hud_box_y + 10
            bullets_rect_width = mag_rect_width * (player.gun.bullets / player.gun.mag_size)
            pg.draw.rect(screen, (100, 100, 100), (mag_rect_x, mag_rect_y, mag_rect_width, mag_rect_height))
            pg.draw.rect(screen, (0, 255, 0), (mag_rect_x, mag_rect_y, bullets_rect_width, mag_rect_height))
            pg.draw.rect(screen, WHITE, (mag_rect_x, mag_rect_y, mag_rect_width, mag_rect_height), 2)
            font = pg.font.Font(None, 36)
            text = font.render(f"{player.gun.bullets} / {player.gun.mag_size}", True, WHITE)
            screen.blit(text, (mag_rect_x + mag_rect_width + 10, mag_rect_y))

            # Draw the magazine label
            label = font.render("Magazine", True, WHITE)
            screen.blit(label, (mag_rect_x + 10, mag_rect_y + 5))

            # Player health bar
            player_health_bar_width = 200
            player_health_bar_height = 30
            player_health_bar_x = hud_box_x + 20
            player_health_bar_y = hud_box_y + 50
            player_health_rect_width = player_health_bar_width * (player_health / player_total_health)
            pg.draw.rect(screen, (100, 100, 100), (player_health_bar_x, player_health_bar_y, player_health_bar_width, player_health_bar_height))
            pg.draw.rect(screen, (255, 0, 0), (player_health_bar_x, player_health_bar_y, player_health_rect_width, player_health_bar_height))
            pg.draw.rect(screen, WHITE, (player_health_bar_x, player_health_bar_y, player_health_bar_width, player_health_bar_height), 2)
            text = font.render(f"{player_health} / {player_total_health}", True, WHITE)
            screen.blit(text, (player_health_bar_x + player_health_bar_width + 10, player_health_bar_y))

            # Draw the health label
            label = font.render("Health", True, WHITE)
            screen.blit(label, (player_health_bar_x + 10, player_health_bar_y + 5))


            # Draw the enemy health bar
            health_bar_width = 200
            health_bar_height = 30
            health_bar_x = 470
            health_bar_y = 250
            health_rect_width = health_bar_width * (enemy.health / total_health)
            pg.draw.rect(screen, RED, (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
            pg.draw.rect(screen, GREEN, (health_bar_x, health_bar_y, health_rect_width, health_bar_height))
            pg.draw.rect(screen, WHITE, (health_bar_x, health_bar_y, health_bar_width, health_bar_height), 2)
            text = font.render(f"{enemy.health} / {total_health}", True, WHITE)
            screen.blit(text, (health_bar_x + health_bar_width + 10, health_bar_y))


            # Draw the enemy using shapes
            pg.draw.circle(screen, 'orange', enemy.rect.center, enemy.rect.width // 2)
            pg.draw.circle(screen, BLACK, enemy.rect.center, enemy.rect.width // 2, 2)  # Add a black border
            pg.draw.circle(screen, WHITE, (enemy.rect.centerx - 30, enemy.rect.centery - 30), 20)  # Left eye
            pg.draw.circle(screen, WHITE, (enemy.rect.centerx + 30, enemy.rect.centery - 30), 20)  # Right eye
            pg.draw.circle(screen, BLACK, (enemy.rect.centerx - 30, enemy.rect.centery - 30), 10)  # Left pupil
            pg.draw.circle(screen, BLACK, (enemy.rect.centerx + 30, enemy.rect.centery - 30), 10)  # Right pupil
            pg.draw.arc(screen, BLACK, (enemy.rect.centerx - 50, enemy.rect.centery, 100, 50), 3.14, 0, 2)  # Mouth

            # Move and draw the player
            player.move()
            player.draw(screen)

            # Update and draw bullets
            for bullet in bullets[:]:
                bullet.update()
                # Check collision with the circular enemy
                if pg.math.Vector2(bullet.rect.center).distance_to(enemy.rect.center) < enemy.rect.width // 2:
                    bullets.remove(bullet)
                    enemy.health -= player.gun.damage
                    if enemy.health <= 0:
                        font = pg.font.Font(None, 72)
                        text = font.render("You Win!", True, GREEN)
                        fade_to_black(screen, text)
                        enemy.health = total_health  # Reset enemy health
                        bullets.clear()
                        boss_attacks.clear()
                        player.gun.bullets = player.gun.mag_size
                        action = show_start_screen()
                        player_total_health = select_difficulty()
                        player_health = player_total_health
                elif bullet.rect.x < 0 or bullet.rect.x > WIDTH or bullet.rect.y < 0 or bullet.rect.y > HEIGHT:
                    bullets.remove(bullet)
                else:
                    bullet.draw(screen)

            # Boss attack patterns
            boss_attack_pattern()

            # Update and draw boss attacks
            for attack in boss_attacks[:]:
                attack.update()
                if attack.rect.colliderect(player.rect):
                    boss_attacks.remove(attack)
                    player_health -= 1
                    if player_health <= 0:
                        font = pg.font.Font(None, 72)
                        text = font.render("Game Over", True, WHITE)
                        fade_to_black(screen, text)
                        boss_attacks.clear()
                        bullets.clear()
                        player.gun.bullets = player.gun.mag_size
                        show_loss_screen()
                elif attack.rect.x < 0 or attack.rect.x > WIDTH or attack.rect.y < 0 or attack.rect.y > HEIGHT:
                    if attack in boss_attacks:
                        boss_attacks.remove(attack)
                else:
                    attack.draw(screen)

            # Update the display
            pg.display.flip()

            # Limit FPS
            pg.time.Clock().tick(60)

            # Prevent the player from moving beyond the window boundaries
            if player.rect.left <= 0:
                player.rect.left = 0
            elif player.rect.right >= WIDTH:
                player.rect.right = WIDTH
            if player.rect.top <= 0:
                player.rect.top = 0
            elif player.rect.bottom >= HEIGHT:
                player.rect.bottom = HEIGHT

    # Quit pygame
    pg.quit()
    sys.exit()