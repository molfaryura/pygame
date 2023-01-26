import sys

import pygame

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption("Destroyer 3000")

icon = pygame.image.load('images/icon.png')

slow_pock = pygame.image.load('images/slow.png')
slow_pock = pygame.transform.scale(slow_pock, (48,48))

pygame.display.set_icon(icon)

x, y = (0, 0)
clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed = pygame.key.get_pressed()

    if pressed[K_UP] and y > 0:
        y-=0.2 * dt
    elif pressed[K_DOWN] and y <= 552:
        y+=0.2 * dt
    elif pressed[K_LEFT] and x > 0 :
        x-=0.2 * dt
    elif pressed[K_RIGHT] and x <= 758:
        x+=0.2 * dt

    screen.fill((0, 0, 0))    
    screen.blit(slow_pock, (x, y))
    pygame.display.update()
