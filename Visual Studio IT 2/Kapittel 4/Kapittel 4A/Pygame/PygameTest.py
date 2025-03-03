'''
Initialization:

pg.init(): Initializes all the Pygame modules.
screen = pg.display.set_mode((800, 600)): Sets up the display window.
clock = pg.time.Clock(): Creates a clock object to manage the frame rate.
start_ticks = pg.time.get_ticks(): Stores the current time in milliseconds when the game starts.


Main Game Loop:

for event in pg.event.get(): Processes events like quitting the game.
current_ticks = pg.time.get_ticks(): Gets the current time in milliseconds.
if current_ticks - start_ticks >= 2500: Checks if 2500 milliseconds (2.5 seconds) have passed since start_ticks.
pg.display.flip(): Updates the display.
clock.tick(60): Caps the frame rate at 60 frames per second.
'''

import time
import pygame as pg
from pygame.locals import *
import math as m

WIDTH, HEIGHT = 650, 400
FPS = 24

RED = (255, 0, 0)
ORANGE = pg.Color('yellow').lerp(pg.Color('red'), 0.7)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)




class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.start_ticks = pg.time.get_ticks()  # Initialize start_ticks here

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)

        pg.draw.line(self.screen, RED, (50, 50), (50, 150), 5)
        pg.draw.rect(self.screen, BLUE, (100, 50, 50, 100), 10)
        pg.draw.rect(self.screen, GREEN, (50, 200, 100, 50), 10)
        pg.draw.circle(self.screen, 'orange', (250, 100), 50)
        pg.draw.circle(self.screen, INDIGO, (250,225), 50, 10)
        pg.draw.ellipse(self.screen, VIOLET, (50, 300, 250, 100))
        pg.draw.arc(self.screen, ORANGE, (50, 450, 250, 100), 0, m.pi, 5)

        current_ticks = pg.time.get_ticks()

        if current_ticks - self.start_ticks >= 2500:
            self.screen.fill("black")

            text = "Game Over"
            font = pg.font.SysFont("Arial", 100)
            text_surface = font.render(text, True, GREEN)
            self.screen.blit(text_surface, (WIDTH/2-200, HEIGHT/2-55))

        pg.display.update()
        

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()

if __name__ == "__main__":
    app = App()
    app.run()

