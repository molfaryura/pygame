"""Tetris 2D Game"""

import pygame

from blocks import Block


def draw_grid(columns, rows, grid_size, x_gap, y_gap):
    """Draws rectangles to fill the screen"""

    for y_pos in range(rows):
        for x_pos in range(columns):
            pygame.draw.rect(screen,
                             (100, 100, 100),
                             [x_pos*grid_size+x_gap, y_pos*grid_size+y_gap, grid_size, grid_size],
                             1)


GRID_SIZE = 30

pygame.init()
screen = pygame.display.set_mode((800, 800))

rows_ = screen.get_height() // GRID_SIZE
cols = screen.get_width() // GRID_SIZE
x_gap_ = (screen.get_width() - cols * GRID_SIZE) // 2
y_gap_ = (screen.get_height() - rows_ * GRID_SIZE) // 2

pygame.display.set_caption('Tetris')

GAME_OVER = False
block = Block(3, 1)
clock = pygame.time.Clock()
fps = 2
while not GAME_OVER:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        block.side_move(-1, cols)
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        block.side_move(1, cols)

    screen.fill((0, 0, 0))

    draw_grid(columns=cols, rows=rows_, grid_size=GRID_SIZE, x_gap=x_gap_, y_gap=y_gap_)
    block.draw_block(GRID_SIZE, x_gap_, y_gap_, screen)

    if event.type != pygame.KEYDOWN:
        block.drop_block(rows_)

    pygame.display.update()

pygame.quit()
