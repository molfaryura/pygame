#!~/pygame/env/bin/python3

"""Tetris 2D Game"""

import pygame

import random

from blocks import Block

GRID_SIZE = 30

pygame.init()
screen = pygame.display.set_mode((800, 800))

rows_ = screen.get_height() // GRID_SIZE
cols = screen.get_width() // GRID_SIZE
x_gap_ = (screen.get_width() - cols * GRID_SIZE) // 2
y_gap_ = (screen.get_height() - rows_ * GRID_SIZE) // 2

pygame.display.set_caption('Tetris')

GAME_OVER = False
block = Block((cols - 1) // 2, 0)
clock = pygame.time.Clock()
fps = 10
game_board = []

for i in range(cols):
    new_col = [(0,0,0) for _ in range(rows_)]
    game_board.append(new_col)

while not GAME_OVER:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
            continue
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        block.side_move(-1, cols)
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        block.side_move(1, cols)
    elif event.type == pygame.KEYDOWN:
        block.drop_block(rows_, game_board)

    screen.fill((0, 0, 0))

    Block.draw_game_board(columns=cols, rows=rows_, screen=screen, game_board=game_board, grid_size=GRID_SIZE, x_gap=x_gap_, y_gap=y_gap_)

    if block:
        block.draw_block(GRID_SIZE, x_gap_, y_gap_, screen)

        if event.type != pygame.KEYDOWN:
            if not block.drop_block(rows_, game_board):
                block = Block(x=random.randint(0, cols - 2), y=0)

    pygame.display.update()

pygame.quit()
