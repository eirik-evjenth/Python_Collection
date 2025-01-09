import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, MOUSEBUTTONDOWN)
import math as m
import time
import random as rnd

colours = ['white', 'green', 'blue', 'red', 'orange', 'violet', 'aqua'] # Farger som er ikke brukt andre steder men for bakgrunn

start_time = time.time()

upgrade = 0
pb = 0
n = 0
WIDTH, HEIGHT = 1280, 720
FPS = 10

class ShopItem:
    def __init__(self, name, cost, effect):
        self.name = name
        self.cost = cost
        self.effect = effect

    def apply_effect(self, app):
        self.effect(app)

def increase_click_value(app):
    app.upgrade += 1

def auto_clicker(app):
    app.auto_clicker_active = True

def double_clicks(app):
    app.double_clicks_active = True

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("clicky (:")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.color = 'pink'
        self.clicks = 0
        self.pb = 0
        self.click_bank = 0
        self.big_x_position = 325
        self.big_y_position = 200
        self.small_x_position = 100
        self.small_y_position = 100
        self.upgrade = 0
        self.auto_clicker_active = False
        self.double_clicks_active = False
        self.shop_items = [
            ShopItem("Stronger clicks", 10, increase_click_value),
            ShopItem("Auto Clicker", 50, auto_clicker),
            ShopItem("Double Clicks", 100, double_clicks)
        ]

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if self.big_x_position < mouse_x < self.big_x_position + 50:
                    if self.big_y_position < mouse_y < self.big_y_position + 50:
                        self.clicks += 1 + self.upgrade
                if self.small_x_position < mouse_x < self.small_x_position + 15:
                    if self.small_y_position < mouse_y < self.small_y_position + 15:
                        self.clicks += 2 + 2 * self.upgrade
                for i, item in enumerate(self.shop_items):
                    if 1080 < mouse_x < 1280 and 135 + i * 40 < mouse_y < 165 + i * 40:
                        if self.click_bank >= item.cost:
                            self.click_bank -= item.cost
                            item.apply_effect(self)

    def update(self):
        self.all_sprites.update()
        if self.auto_clicker_active:
            self.clicks += 1
        if self.double_clicks_active:
            self.clicks *= 2

    def draw(self):
        self.screen.fill(self.color)
        self.all_sprites.draw(self.screen)


        # Draw jungle background
        pg.draw.rect(self.screen, (34, 139, 34), (0, 0, WIDTH, HEIGHT))  # Green background for jungle


        font = pg.font.Font(None, 60)
        text = font.render(f"{self.clicks} Clicks!", True, 'black')
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 0))

        font = pg.font.Font(None, 40)
        text = font.render("Shop:", True, 'black')
        self.screen.blit(text, (WIDTH - text.get_width() - 70, 100))

        for i, item in enumerate(self.shop_items):
            font_upgrades = pg.font.Font(None, 30)
            text1 = font_upgrades.render(f"{item.name}: {item.cost}", True, 'black')
            pg.draw.rect(self.screen, self.color, (1070, 135 + i * 40, text1.get_width() + 20, text1.get_height()))
            self.screen.blit(text1, (WIDTH - text1.get_width() - 10, 110 + text.get_height() + i * 40))

        text2 = font.render(f"{round(self.click_bank, 1)} clicks stored", True, 'black')
        self.screen.blit(text2, (WIDTH // 2 - text.get_width() // 2 - 50, 50))

        font = pg.font.Font(None, 20)
        text = font.render(f"current multiplier = {self.upgrade + 1}", True, 'black')
        self.screen.blit(text, (0, 0))

        
        # Draw small banana
        pg.draw.ellipse(self.screen, (255, 255, 0), (self.small_x_position, self.small_y_position, 15, 5))  # Banana


        # Draw big monkey
        pg.draw.circle(self.screen, (139, 69, 19), (self.big_x_position + 25, self.big_y_position + 25), 25)  # Body
        pg.draw.circle(self.screen, (160, 82, 45), (self.big_x_position + 25, self.big_y_position + 15), 10)  # Head
        pg.draw.circle(self.screen, (0, 0, 0), (self.big_x_position + 20, self.big_y_position + 15), 2)  # Left eye
        pg.draw.circle(self.screen, (0, 0, 0), (self.big_x_position + 30, self.big_y_position + 15), 2)  # Right eye


        pg.display.update()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

            current_time = time.time()
            if round((current_time - start_time), 1) % 2 == 0:
                global n
                n += 1

                self.color = rnd.choice(colours)
                self.big_x_position = rnd.randint(0, 600)
                self.big_y_position = rnd.randint(0, 350)
                self.small_x_position = rnd.randint(0, 635)
                self.small_y_position = rnd.randint(0, 385)

                if self.clicks > self.pb:
                    print(f"You got a new personal best amount of clicks at {self.clicks} times in round {n}")
                    self.pb = self.clicks
                else:
                    print(f"You were able to click {self.clicks} times in round {n}")

                self.click_bank += round((0.1 * self.clicks), 1)
                self.clicks = 0
        pg.quit()

        if not self.running:
            print(f"You have closed the game. Your personal best was {self.pb} clicks in the given time")
        global pb
        pb = self.pb
        pb = str(pb)

if __name__ == "__main__":
    app = App()
    app.run()
