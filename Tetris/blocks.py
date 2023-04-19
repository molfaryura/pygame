"""A class for creating blocks"""

from pygame import draw

BLOCKS = [
    [[1, 4, 7], [3, 4, 5]], # straight
    [[1, 3, 4, 5, 7]], # cross
    [[0, 1, 4, 5], [1, 3, 4, 6]], # two on two 1
    [[1, 2, 3, 4]], [0, 3, 4, 7], # two on two 2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]], # L 1
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]], # L 2
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]] # one on three
]

class Block:
    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y
        self.type = 0
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
    def drop_block(self, rows):
        can_drop = True
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape() and self.y + y >= rows -1:
                    can_drop = False
        if can_drop:
            self.y += 1

    def side_move(self, dx, cols):
        can_move = True
        for y in range(3):
            for x in range(3):
                if ((y * 3 + x in self.shape()) and (x + self.x >= cols - 1 and dx == 1)
                    or (y * 3 + x in self.shape()) and (x + self.x < 1 and dx == -1)):
                    can_move = False
        if can_move:
            self.x += dx
