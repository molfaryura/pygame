import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breaking Bricks")

#Loading paddle image
paddle = pygame.image.load('Breaking bricks/images/paddle.png')
paddle = paddle.convert_alpha()
paddle_rect = paddle.get_rect()

#Loading ball image
ball = pygame.image.load('Breaking bricks/images/ball.png')
ball = paddle.convert_alpha()
ball_rect = ball.get_rect()

#Loading brick image
brick = pygame.image.load('Breaking bricks/images/brick.png')
brick = brick.convert_alpha()
brick = pygame.transform.scale(brick, (48,48))
brick_rect = brick.get_rect()
bricks = []
brick_rows = 3
brick_gap = 10
brick_cols = screen.get_width()//(brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap)//2

for y in range(brick_rows):
    brickY = y * (brick_rect[3]+brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2]+brick_gap) + side_gap
        bricks.append((brickX, brickY))

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)
    screen.fill((0,0,0))

    for b in bricks:
        screen.blit(brick, b)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()