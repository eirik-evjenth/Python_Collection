import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 650, 400
FPS = 24


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Stein, saks, papir")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.color = "white"
        self.rect = pg.Rect(100, 100, 50, 50)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.screen.fill("black")
        self.stone = pg.draw.rect(self.screen, self.color, self.rect)
        self.all_sprites.draw(self.screen, self.stone)
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
