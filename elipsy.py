import pygame, sys
import random

from pygame.locals import *


#podstawy

rozmiar = 800
bok = 30


pygame.init()
plansza = pygame.display.set_mode((rozmiar, rozmiar))
pygame.display.set_caption('Elipsy')


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BAD_GREEN = (129, 187, 129)
GRAY = (200, 200, 200)
LIGHT_GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (176, 224, 230)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
PINK = (255, 105, 180)
ORANGE = (255, 140, 0)


FPS = 10000000
fpsClock = pygame.time.Clock()

G = 6.67 * 10 ** (-11)

class planet:
    def __init__(self, x, y, m, r, v):
        self.x = x
        self.y = y
        self.m = m
        self.r = r
        self.v = v

    def move(self, F, sin, cos):
        a = F / self.m
        ax = a * cos
        ay = a * sin
        self.v[0] = self.v[0] + ax * dt
        self.v[1] = self.v[1] + ay * dt
        self.x = self.x + self.v[0] * dt + 0.5 * ax * dt ** 2
        self.y = self.y + self.v[1] * dt + 0.5 * ay * dt ** 2
        

    def show(self, plansza):
        pygame.draw.circle(plansza, WHITE, (self.x, self.y), self.r)


r = 200
dt = 0.01

sun = planet(rozmiar/2, rozmiar/2, 50000000000000, 10, [0, 0])
earth = planet(sun.x + r, sun.y, 100, 5, [0, -3])


while True:
    plansza.fill(BLACK)

    sun.show(plansza)
    earth.show(plansza)

    dx = sun.x - earth.x
    dy = sun.y - earth.y
    r = dx ** 2 + dy ** 2
    F = G * sun.m * earth.m / r
    r = r ** 0.5

    sin = dy / r
    cos = dx / r

    sun.move(F, -sin, -cos)
    earth.move(F, sin, cos)




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
