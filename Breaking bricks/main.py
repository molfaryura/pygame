'''
A 2D game in which the player 
destroys bricks by bouncing a ball
'''

import sys

import pygame

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breaking Bricks")

#Loading paddle image
paddle = pygame.image.load('Breaking bricks/images/paddle.png')
paddle = paddle.convert_alpha()
paddle_rect = paddle.get_rect()
paddle_rect[1] = screen.get_height() - 100

#Loading ball image
ball = pygame.image.load('Breaking bricks/images/ball.png')
ball = paddle.convert_alpha()
ball_rect = ball.get_rect()

#Loading brick image
brick = pygame.image.load('Breaking bricks/images/brick.png')
brick = brick.convert_alpha()
brick = pygame.transform.scale(brick, (48,48))

#Create rows, columns, and gaps
brick_rect = brick.get_rect()
bricks = []
brick_rows = 3
brick_gap = 10
brick_cols = screen.get_width()//(brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap)//2

#Brick images will fill all screen
#with 3 rows
for y in range(brick_rows):
    brickY = y * (brick_rect[3]+brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2]+brick_gap) + side_gap
        bricks.append((brickX, brickY))

#Object to track time 
clock = pygame.time.Clock()

while True:
    dt = clock.tick(60) # max 60 frames per second

    #Blit all screen width with bricks
    for b in bricks:
        screen.blit(brick, b)

    #Put paddle in the left corner    
    screen.blit(paddle, paddle_rect)

    #Initialize key pressing in the game
    pressed = pygame.key.get_pressed()

    #Move paddle by pressing keys
    if pressed[K_LEFT] and paddle_rect[0] > 0:
            paddle_rect[0]-=0.3 * dt
    elif pressed[K_RIGHT] and paddle_rect[0] < 800 - 128:
            paddle_rect[0]+=0.3 * dt

    #Correct exit if user press on quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()
    screen.fill((0,0,0))

