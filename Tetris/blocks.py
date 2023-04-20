#!~/pygame/env/bin/python3

"""A class for creating blocks"""

import random

from pygame import draw

BLOCKS = [
    [[1, 4, 7], [3, 4, 5]], # straight
    [[1, 3, 4, 5, 7]], # cross
    [[0, 1, 4, 5], [1, 3, 4, 6]], # two on two 1
    [[1, 2, 3, 4], [0, 3, 4, 7]], # two on two 2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]], # L 1
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]], # L 2
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]] # one on three
]

class Block:
    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y
        self.type = random.randint(0,6)
        self.rotation = 0

    def shape(self):
        return BLOCKS[self.type][self.rotation]
    
    def draw_block(self, grid_size, x_gap, y_gap, screen):
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape():
                    draw.rect(screen, (255, 255, 255),
                                    [(x + self.x) * grid_size + x_gap + 1,
                                    (y + self.y) * grid_size + y_gap + 1,
                                    grid_size, grid_size])

    def drop_block(self, rows, game_board):
        can_drop = True
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape() and self.y + y >= rows -1:
                    can_drop = False
        if can_drop:
            self.y += 1
        else:
            for y in range(3):
                for x in range(3):
                    if y * 3 + x in self.shape():
                        game_board[x + self.x][y + self.y] = (0, 255, 0)
        return can_drop

    def side_move(self, dx, cols):
        can_move = True
        for y in range(3):
            for x in range(3):
                if ((y * 3 + x in self.shape()) and (x + self.x >= cols - 1 and dx == 1)
                    or (y * 3 + x in self.shape()) and (x + self.x < 1 and dx == -1)):
                    can_move = False
        if can_move:
            self.x += dx

    @staticmethod
    def draw_game_board(columns, rows, screen, game_board, grid_size, x_gap, y_gap):
        """Draws a game board"""

        for y_pos in range(rows):
            for x_pos in range(columns):
                draw.rect(screen,
                                (100, 100, 100),
                                [x_pos*grid_size+x_gap, y_pos*grid_size+y_gap, grid_size, grid_size],
                                1)
                if game_board[x_pos][y_pos] != (0, 0, 0): 
                    draw.rect(screen, game_board[x_pos][y_pos],
                            [x_pos*grid_size+x_gap + 1, y_pos*grid_size+y_gap + 1, grid_size - 1, grid_size -1])
