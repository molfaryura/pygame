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

screen = display.set_mode((600, 800))
display.set_caption('Tetris')

ROWS = 800 // GRID_SIZE
COLS = 600 // GRID_SIZE
x_gap_ = (screen.get_width() - COLS * GRID_SIZE) // 2
y_gap_ = (screen.get_height() - ROWS * GRID_SIZE) // 2

game_board = []


for i in range(COLS):
    new_col = [(0,0,0) for _ in range(ROWS)]
    game_board.append(new_col)


class Block:
    """ A class representing a block in a Tetris game.

    Attributes:
    -----------
    x_cor : int
        The x-coordinate of the block's position.
    y_cor : int
        The y-coordinate of the block's position.
    type : int
        The type of the block (0-6).
    rotation : int
        The current rotation of the block (0-3).
    color : tuple
        The color of the block in RGB format.

    Methods:
    --------
    shape() -> list:
        Returns a list of positions that the block occupies.
    draw_block() -> None:
        Draws the block on the screen.
    collides(n_x: int, n_y: int) -> bool:
        Returns True if the block collides with the game board at the specified position.
    drop_block() -> bool:
        Drops the block by one unit if it is able to, and returns True. If it is not able to drop,
        the block is added to the game board and False is returned.
    side_move(d_x: int) -> None:
        Moves the block horizontally by the specified amount.
    draw_game_board() -> None:
        Draws the game board on the screen.
    rotate() -> None:
        Rotates the block by 90 degrees if it is able to.
    find_lines() -> int:
        Removes an_y completed lines from the game board and returns the number of lines removed.
    """

    def __init__(self, x_cor , y_cor) -> None:
        """Initializes a new block object with the specified position."""

        self.x_cor = x_cor
        self.y_cor = y_cor
        self.type = random.randint(0,6)
        self.rotation = 0
        self.color = random.choice(COLORS)

    def shape(self) -> list:
        """Returns a list of positions that the block occupies."""

        return BLOCKS[self.type][self.rotation]

    def draw_block(self) -> None:
        """Draws the block on the screen."""

        for y_pos in range(3):
            for x_pos in range(3):
                if y_pos * 3 + x_pos in self.shape():
                    draw.rect(screen, self.color,
                                    [(x_pos + self.x_cor) * GRID_SIZE + x_gap_ + 1,
                                    (y_pos + self.y_cor) * GRID_SIZE + y_gap_ + 1,
                                    GRID_SIZE, GRID_SIZE])


    def collides(self, n_x, n_y) -> bool:
        """Returns True if the block collides with the game board at the specified position.

        Parameters:
        -----------
        n_x : int
            The amount to move the block in the x-direction.
        n_y : int
            The amount to move the block in the y-direction.
        """

        collision = False
        for y_pos in range(3):
            for x_pos in range(3):
                if y_pos * 3 + x_pos in self.shape():
                    if (x_pos + self.x_cor + n_x < 0 or x_pos + self.x_cor + n_x > COLS -1) or \
                        (y_pos + self.y_cor + n_y < 0 or y_pos + self.y_cor + n_y > ROWS - 1) or \
                        (game_board[x_pos + self.x_cor + n_x][y_pos + self.y_cor + n_y]
                         != (0, 0, 0)):
                        collision = True
                        break
        return collision

    def drop_block(self) -> bool:
        """Drops the block by one unit if it is able to, and returns True. If it is not able
        to drop, the block is added to the game board and False is returned.
        """

        can_drop = True
        for y_pos in range(3):
            for x_pos in range(3):
                if y_pos * 3 + x_pos in self.shape() and self.collides(n_x=0, n_y=1):
                    can_drop = False

        if can_drop:
            self.y_cor += 1
        else:
            for y_pos in range(3):
                for x_pos in range(3):
                    if y_pos * 3 + x_pos in self.shape():
                        if y_pos * 3 + x_pos in self.shape():
                            game_board[x_pos + self.x_cor][y_pos + self.y_cor] = self.color

        return can_drop

    def side_move(self, d_x) -> None:
        """Moves the block horizontally by the specified amount.

        Parameters:
        -----------
        d_x : int
            The amount to move the block in the x-direction.
        """

        can_move = True
        for y_pos in range(3):
            for x_pos in range(3):
                if y_pos * 3 + x_pos in self.shape() and self.collides(d_x, 0):
                    can_move = False
        if can_move:
            self.x_cor += d_x

    @staticmethod
    def draw_game_board() -> None:
        """Draws a game board"""

        for y_pos in range(ROWS):
            for x_pos in range(COLS):
                draw.rect(screen,
                                (100, 100, 100),
                                [x_pos * GRID_SIZE + x_gap_, y_pos * GRID_SIZE + y_gap_,
                                 GRID_SIZE, GRID_SIZE], 1)
                if game_board[x_pos][y_pos] != (0, 0, 0):
                    draw.rect(screen, game_board[x_pos][y_pos],
                            [x_pos * GRID_SIZE + x_gap_ + 1, y_pos * GRID_SIZE + y_gap_ + 1,
                             GRID_SIZE - 1, GRID_SIZE -1])

    def rotate(self) -> None:
        """Rotates the block by 90 degrees if it is able to."""

        last_rotation = self.rotation
        self.rotation = (self.rotation + 1) % len(BLOCKS[self.type])
        can_rotate = True
        for y_pos in range(3):
            for x_pos in range(3):
                if y_pos * 3 + x_pos in self.shape():
                    if self.collides(n_x=0, n_y=0):
                        can_rotate = False

        if not can_rotate:
            self.rotation = last_rotation

    @staticmethod
    def find_lines() -> int:
        """ Removes an_y completed lines from the game board and
        returns the number of lines removed.
        """

        lines = 0
        for y_pos in range(ROWS):
            empty = 0
            for x_pos in range(COLS):
                if game_board[x_pos][y_pos] == (0, 0, 0):
                    empty += 1
            if not bool(empty):
                lines += 1
                for y_pos_ in range(y_pos, 1, -1):
                    for x_pos_ in range(COLS):
                        game_board[x_pos_][y_pos_] = game_board[x_pos_][y_pos - 1]
        return lines
