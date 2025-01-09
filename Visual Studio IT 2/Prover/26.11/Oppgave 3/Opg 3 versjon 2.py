import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, MOUSEBUTTONDOWN)
import math as m
import time
import random as rnd

colours = ['white', 'green', 'blue', 'red', 'orange', 'violet', 'pink']

start_time = time.time()

pb = 0
n = 0
WIDTH, HEIGHT = 650, 400
FPS = 10

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("clicky (:")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.color = rnd.choice(colours)
        self.clicks = 0
        self.pb = 0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                self.clicks += 1


    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(self.color)
        self.all_sprites.draw(self.screen)
        
        global clicks
        font = pg.font.Font(None, 72)
        text = font.render(f"{self.clicks} clicks", True, 'black')
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pg.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


            current_time = time.time()
            if round((current_time - start_time),1) % 2 == 0:
                
                global n
                n += 1  # antall runder

                self.color = rnd.choice(colours)

                if self.clicks > self.pb:
                    print(f"You got a new personal best amount of clicks at {self.clicks} times in round {n}")
                    self.pb = self.clicks
                else:
                    print(f"You were able to click {self.clicks} times in round {n}")

                self.clicks = 0
        pg.quit()

        if self.running == False:
            print(f"You have closed the game. Your personal best was {self.pb} clicks in the given time")
        global pb
        pb = self.pb
if __name__ == "__main__":
    app = App()
    app.run()

    with open("Prover/26.11/Oppgave 3/pb.txt", "w") as file:
        file.write(f"Your personal best clicks was {pb} clicks")

