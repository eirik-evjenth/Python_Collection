import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, MOUSEBUTTONDOWN)
import math as m
import time

start_time = time.time()

WIDTH, HEIGHT = 650, 400
FPS = 24
clicks = 0

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("clicky (:")
        self.running = True
        self.all_sprites = pg.sprite.Group()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                global clicks
                clicks += 1


    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("white")
        self.all_sprites.draw(self.screen)
        
        global clicks
        font = pg.font.Font(None, 72)
        text = font.render(f"{clicks} clicks", True, 'black')
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pg.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

            current_time = time.time()
            if current_time - start_time > 10:
                self.running = False
        pg.quit()

if __name__ == "__main__":
    app = App()
    app.run()

print(f"You were able to click {clicks} times")