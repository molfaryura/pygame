"""Tetris 2D Game"""

import pygame


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
while not GAME_OVER:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True

    screen.fill((0, 0, 0))

    draw_grid(columns=cols, rows=rows_, grid_size=GRID_SIZE, x_gap=x_gap_, y_gap=y_gap_)

    pygame.display.update()

pygame.quit()
