#!~/pygame/env/bin/python3

"""A class for creating blocks"""

import random

from pygame import draw, display

BLOCKS = [
    [[1, 4, 7], [3, 4, 5]], # straight
    [[1, 3, 4, 5, 7]], # cross
    [[0, 1, 4, 5], [1, 3, 4, 6]], # two on two 1
    [[1, 2, 3, 4], [0, 3, 4, 7]], # two on two 2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]], # L 1
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]], # L 2
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]] # one on three
]

COLORS = [
  (255, 0, 0),    # Red
  (0, 255, 0),    # Green
  (0, 0, 255),    # Blue
  (255, 255, 0),  # Yellow
  (255, 0, 255),  # Magenta
  (0, 255, 255),  # Cyan
  (128, 0, 0),    # Maroon
  (0, 128, 0),    # Dark Green
  (0, 0, 128),    # Navy
  (128, 128, 0),  # Olive
  (128, 0, 128),  # Purple
  (0, 128, 128)   # Teal
]

GRID_SIZE = 30

screen = display.set_mode((800, 800))
display.set_caption('Tetris')

rows_ = screen.get_height() // GRID_SIZE
cols = screen.get_width() // GRID_SIZE
x_gap_ = (screen.get_width() - cols * GRID_SIZE) // 2
y_gap_ = (screen.get_height() - rows_ * GRID_SIZE) // 2

game_board = []

for i in range(cols):
    new_col = [(0,0,0) for _ in range(rows_)]
    game_board.append(new_col)


class Block:
    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y
        self.type = random.randint(0,6)
        self.rotation = 0
        self.color = random.choice(COLORS)

    def shape(self):
        return BLOCKS[self.type][self.rotation]
    
    def draw_block(self):
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape():
                    draw.rect(screen, self.color,
                                    [(x + self.x) * GRID_SIZE + x_gap_ + 1,
                                    (y + self.y) * GRID_SIZE + y_gap_ + 1,
                                    GRID_SIZE, GRID_SIZE])


    def collides(self, nx, ny):
        collision = False
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape():
                    if x + self.x + nx < 0 or x + self.x + nx > cols -1:
                        collision = True
                        break
                    if y + self.y + ny < 0 or y + self.y + ny > rows_ -1:
                        collision = True
                        break
                    if game_board[x + self.x + nx][y + self.y + ny] != (0, 0, 0):
                        collision = True
                        break
        return collision

    def drop_block(self):
        can_drop = True
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape() and self.collides(nx=0, ny=1):
                    can_drop = False

        if can_drop:
            self.y += 1
        else:
            for y in range(3):
                for x in range(3):
                    if y * 3 + x in self.shape():
                        game_board[x + self.x][y + self.y] = self.color

        return can_drop

    def side_move(self, dx):
        can_move = True
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape() and self.collides(dx, 0):
                    can_move = False
        if can_move:
            self.x += dx

    @staticmethod
    def draw_game_board():
        """Draws a game board"""

        for y_pos in range(rows_):
            for x_pos in range(cols):
                draw.rect(screen,
                                (100, 100, 100),
                                [x_pos*GRID_SIZE+x_gap_, y_pos*GRID_SIZE+y_gap_, GRID_SIZE, GRID_SIZE],
                                1)
                if game_board[x_pos][y_pos] != (0, 0, 0): 
                    draw.rect(screen, game_board[x_pos][y_pos],
                            [x_pos*GRID_SIZE+x_gap_ + 1, y_pos*GRID_SIZE+y_gap_ + 1, GRID_SIZE - 1, GRID_SIZE -1])

    def rotate(self):
        last_rotation = self.rotation
        self.rotation = (self.rotation + 1) % len(BLOCKS[self.type])
        can_rotate = True
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape():
                    if self.collides(nx=0, ny=0):
                        can_rotate = False

        if not can_rotate:
            self.rotation = last_rotation

    def find_lines(self):
        lines = 0
        for y in range(rows_):
            empty = 0
            for x in range(cols):
                if game_board[x][y] == (0, 0, 0):
                    empty += 1
            if not bool(empty):
                lines += 1
                for y_ in range(y, 1, -1):
                    for x_ in range(cols):
                        game_board[x_][y_] = game_board[x_][y_ - 1]
        return lines
    
