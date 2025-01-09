import pygame as pg
import random
import math
import time

pg.init()
pg.mixer.init()
pg.mixer.music.load('tone.mp3')
WIDTH = 600
HEIGHT = 600
start_time = time.time()

BLACK = (0, 0, 0)

class GameScreen:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.hidden_object = HiddenObject(self.screen)

    def draw(self):
        self.screen.fill(BLACK)
        pg.draw.rect(self.screen, (0, 0, 0), (self.hidden_object.x, self.hidden_object.y, 50, 50))
        # teikn det skjulte objektet for debugging ...
        pg.display.flip()

    def handle_click(self, pos):
        if self.hidden_object.is_clicked(pos):
            print("Gratulerar, du fant det skjulte objektet!")

class HiddenObject:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 600)
        self.speed = 5

    def move(self):
        self.x = (self.x + random.choice([-1, 1]) * self.speed) % 600
        self.y = (self.y + random.choice([-1, 1]) * self.speed) % 600

    def play_sound(self, pos):
        distance = math.hypot(self.x - pos[0], self.y - pos[1])
        max_distance = math.hypot(WIDTH, HEIGHT)
        volume = max(0, 1 - (distance / max_distance))
        pg.mixer.music.set_volume(volume)
        # Juster lydstyrken etter avstanden til det skjulte objektet ...

    def get_pos(self):
        return self.x, self.y


    def is_clicked(self, pos):
        return math.hypot(self.x - pos[0], self.y - pos[1]) < 50

def main():
    game_screen = GameScreen()
    running = True

    pg.mixer.music.play()

    # Starttidspunkt for spelet ..
    #runtime = ... # Lengde på lydsample = tida du har på å finne det skjulte objektet

    # Ved oppstart av spelet, spel av lydfila tone.mp3 ..

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                game_screen.handle_click(pg.mouse.get_pos())
                if game_screen.hidden_object.is_clicked(pg.mouse.get_pos()):
                    endtime = time.time()
                    font = pg.font.Font(None, 60)
                    text = font.render(f"You Win!, it took {round(endtime - start_time, 1)} seconds", True, (0, 255, 0))
                    game_screen.screen.blit(text, (20, HEIGHT // 2))
                    pg.display.flip()
                    time.sleep(4)
                    running = False
                # Avslutt spelet og skriv ut kor lang tid det tok å finne det skjulte objektet
            if time.time() - start_time > 20:
                pg.draw.rect(game_screen.screen, (255, 0, 0), (game_screen.hidden_object.x, game_screen.hidden_object.y, 50, 50))
                font = pg.font.Font(None, 100)
                text = font.render(f"You Lose", True, (255, 255, 255))
                game_screen.screen.blit(text, (150, HEIGHT // 2))
                pg.display.flip()
                time.sleep(4)
                running = False
        # Dersom tida er ute, avslutt spelet ...

        game_screen.hidden_object.move()
        game_screen.hidden_object.play_sound(pg.mouse.get_pos())
        game_screen.draw()
        game_screen.clock.tick(60)

if __name__ == "__main__":
    main()