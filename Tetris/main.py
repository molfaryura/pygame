#!~/pygame/env/bin/python3

"""Tetris 2D Game"""

import random

import pygame

from blocks import Block, screen, COLS

pygame.init()

block = Block((COLS - 1) // 2, 0)
clock = pygame.time.Clock()
FPS = 10

SCORE = 0
font = pygame.font.SysFont('Times New Roman', 35, True)

font_game_over = pygame.font.SysFont('Times New Roman', 60, True)
text_game_over = font_game_over.render('Game Over', True, (255, 255, 255))
text_game_over_pos = ((screen.get_width() - text_game_over.get_width())//2,
                      (screen.get_height() - text_game_over.get_height())//2)

GAME_FINISHED = False

GAME_OVER = False
while not GAME_OVER:
    clock.tick(FPS)
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
                SCORE += Block.find_lines()
                FPS += 0.2
                block = Block(x_cor=random.randint(5, COLS - 5), y_cor=0)
                if block.collides(n_x=0, n_y=0):
                    GAME_FINISHED = True

    text = font.render(f'SCORE: {str(SCORE)}', True, (255, 255, 255))
    screen.blit(text, [10, 10])

    if GAME_FINISHED:
        screen.blit(text_game_over, text_game_over_pos)

    pygame.display.update()

pygame.quit()
