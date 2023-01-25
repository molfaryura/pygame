import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

while True:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

