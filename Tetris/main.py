#!~/pygame/env/bin/python3

"""Tetris 2D Game"""

import pygame

import random

from blocks import Block, screen, cols

GRID_SIZE = 30

pygame.init()

block = Block((cols - 1) // 2, 0)
clock = pygame.time.Clock()
fps = 10

score = 0
font = pygame.font.SysFont('Times New Roman', 35, True)

font_game_over = pygame.font.SysFont('Times New Roman', 60, True)
text_game_over = font_game_over.render('Game Over', True, (255, 255, 255))
text_game_over_pos = ((screen.get_width() - text_game_over.get_width())//2,
                      (screen.get_height() - text_game_over.get_height())//2)

GAME_FINISHED = False
GAME_OVER = False
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
            if not block.drop_block() and not GAME_FINISHED:
                score += block.find_lines()
                block = Block(x=random.randint(0, cols - 2), y=0)
                if block.collides(0, 0):
                    GAME_FINISHED = True

    text = font.render(f'Score: {str(score)}', True, (255, 255, 255))
    screen.blit(text, [10, 10])

    if GAME_FINISHED:
        screen.blit(text_game_over, text_game_over_pos)

    pygame.display.update()

pygame.quit()
