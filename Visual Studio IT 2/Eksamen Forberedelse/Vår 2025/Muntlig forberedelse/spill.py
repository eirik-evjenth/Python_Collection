import pygame as pg
pg.init()

# Skjermoppsett
bredde, høyde = 600, 400
vindu = pg.display.set_mode((bredde, høyde))
pg.display.set_caption("Pygame-spill")

# Klasser
class Spiller:
    def __init__(self, x, y, bredde, høyde, farge):
        self.rect = pg.Rect(x, y, bredde, høyde)
        self.farge = farge
        self.fart = 5

    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, self.rect)

    def flytt(self, taster):
        if taster[pg.K_LEFT]:
            self.rect.x -= self.fart
        if taster[pg.K_RIGHT]:
            self.rect.x += self.fart
        if taster[pg.K_UP]:
            self.rect.y -= self.fart
        if taster[pg.K_DOWN]:
            self.rect.y += self.fart

# Spillobjekt
spiller = Spiller(100, 100, 50, 50, (0, 128, 255))

# Spill-løkke
klokke = pg.time.Clock()
kjører = True

while kjører:
    klokke.tick(60)
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            kjører = False

    taster = pg.key.get_pressed()
    spiller.flytt(taster)

    if spiller.rect.left < 0:
        spiller.rect.left = 0
    if spiller.rect.right > bredde:
        spiller.rect.right = bredde
    if spiller.rect.top < 0:
        spiller.rect.top = 0
    if spiller.rect.bottom > høyde:
        spiller.rect.bottom = høyde

    vindu.fill((30, 30, 30))  # Bakgrunn
    spiller.tegn(vindu)
    pg.display.flip()

pg.quit()
