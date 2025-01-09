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

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("clicky (:")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.color = 'pink'                  # Gjør det vanskelig å se den på starten, så aldri blir rosa igjen
        self.clicks = 0
        self.pb = 0
        self.click_bank = 0
        self.big_x_position = 325
        self.big_y_position = 200

        self.small_x_position = 100
        self.small_y_position = 100

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos 
                global upgrade
                if self.big_x_position < mouse_x < self.big_x_position + 50:       # Kan gjøre dettte på en linje, men var altfor lang
                    if self.big_y_position < mouse_y < self.big_y_position + 50:
                        self.clicks += 1 + upgrade
                if self.small_x_position < mouse_x < self.small_x_position + 15:   
                    if self.small_y_position < mouse_y < self.small_y_position + 15:
                        self.clicks += 2 + 2 * upgrade
                if 1080 < mouse_x < 1280: 
                    if 135 < mouse_y < 165:
                        if self.click_bank > 10 + upgrade * 5:
                            self.click_bank -= 10 + upgrade * 5
                            upgrade += 1
                        


    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(self.color)
        self.all_sprites.draw(self.screen)
        

        
        global clicks
        font = pg.font.Font(None, 60)
        text = font.render(f"{self.clicks} Clicks!", True, 'black')
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 0))

        font = pg.font.Font(None, 40)
        text = font.render("Shop:", True, 'black')
        self.screen.blit(text, (WIDTH-text.get_width()-70, 100))

        font_upgrades = pg.font.Font(None, 30)
        text1 = font_upgrades.render(f"Stronger clicks: {10+upgrade*5}", True, 'black')

        pg.draw.rect(self.screen, self.color, (1070, 135, text1.get_width()+20, text1.get_height())) # Hitbox til upgrade
        self.screen.blit(text1, (WIDTH - text1.get_width()-10, 110 + text.get_height()))

        text2 = font.render(f"{round(self.click_bank,1)} clicks stored", True, 'black')
        self.screen.blit(text2, (WIDTH // 2 - text.get_width() // 2 - 50, 50))

        font = pg.font.Font(None, 20)
        text = font.render(f"current multiplier = {upgrade+1}", True, 'black')
        self.screen.blit(text, (0, 0))


        pg.draw.rect(self.screen, 'pink', (self.small_x_position, self.small_y_position, 15, 15)) # rosa er vanskelig å se
        pg.draw.rect(self.screen, 'brown', (self.big_x_position, self.big_y_position, 50, 50))    # brun er lett å se


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

                self.big_x_position = rnd.randint(0, 600)
                self.big_y_position = rnd.randint(0, 350)

                self.small_x_position = rnd.randint(0, 635)
                self.small_y_position = rnd.randint(0, 385)

                if self.clicks > self.pb:
                    print(f"You got a new personal best amount of clicks at {self.clicks} times in round {n}")
                    self.pb = self.clicks
                else:
                    print(f"You were able to click {self.clicks} times in round {n}")

                self.click_bank += round((0.1 * self.clicks),1)
                self.clicks = 0
        pg.quit()

        if self.running == False:
            print(f"You have closed the game. Your personal best was {self.pb} clicks in the given time")
        global pb
        pb = self.pb
        pb = str(pb)
        
if __name__ == "__main__":
    app = App()
    app.run()




'''
Litt om spillet før du spiller, er ikke så viktig

Det er two kvadrater som teleporterer rundt om kring hvert andre sekund, 
jeg synes det burde være en mer "risky" kvadrat som gir mer men er vanskligere å treffe
Man kan få clicks også vil personlig rekord måles, en tidel av total clicks vil være
gitt i en slags "bank" også kan man bruke disse på å oppgradere antall clicks man får.

Man får en "multiplier" på antall clicks som gjør at jo lengre man spiller jo større blir
antall clicks man får, jeg har gjort noe å unngå dette men er ikke helt perfekt.
'''