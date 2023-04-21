#!~/pygame/env/bin/python3

"""Tetris 2D Game"""

import pygame

import random

from blocks import Block, screen, cols

GRID_SIZE = 30

pygame.init()

GAME_OVER = False
block = Block((cols - 1) // 2, 0)
clock = pygame.time.Clock()
fps = 5

while not GAME_OVER:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
            continue

    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        block.side_move(-1)
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        block.side_move(1)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            block.drop_block()
        elif event.key == pygame.K_UP:
            block.rotate()
            block.drop_block()

    screen.fill((0, 0, 0))

    Block.draw_game_board()

    if block:
        block.draw_block()

        if event.type != pygame.KEYDOWN:
            if not block.drop_block():
                block = Block(x=random.randint(0, cols - 2), y=0)

    pygame.display.update()

pygame.quit()
