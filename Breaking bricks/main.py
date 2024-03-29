"""A 2D game in which the player destroys bricks by bouncing a ball"""

import sys

import os

import pygame

from pygame.locals import *

pygame.init()

try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy"

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breaking Bricks")

#Loading paddle image
paddle = pygame.image.load('./images/paddle.png')
paddle = paddle.convert_alpha()
paddle_rect = paddle.get_rect()
paddle_rect[1] = screen.get_height() - 100
paddle_rect[0] = (screen.get_width() - paddle_rect.width)//2

#Loading ball image
ball = pygame.image.load('./images/ball.png')
ball = ball.convert_alpha()
ball = pygame.transform.scale(ball, (24,24))
ball_rect = ball.get_rect()

ball_start = (180, 250 )
ball_speed = (3.0, 3.0)
BALL_SERVED = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

#Loading brick image
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick = pygame.transform.scale(brick, (48,48))

#Create rows, columns, and gaps
brick_rect = brick.get_rect()
bricks = []
BRICK_ROWS = 4
BRICK_GAP = 10
brick_cols = screen.get_width()//(brick_rect[2] + BRICK_GAP)
side_gap = (screen.get_width() - (brick_rect[2] + BRICK_GAP) * brick_cols + BRICK_GAP)//2

#Brick images will fill all screen
#with 4 rows
for y in range(BRICK_ROWS):
    brickY = y * (brick_rect[3]+BRICK_GAP)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2]+BRICK_GAP) + side_gap
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
    screen.blit(ball, ball_rect)

    #Initialize key pressing in the game
    pressed = pygame.key.get_pressed()

    #Move paddle by pressing keys
    if pressed[K_LEFT] and paddle_rect[0] > 0:
        paddle_rect[0]-=0.3 * dt
    elif pressed[K_RIGHT] and paddle_rect[0] < 800 - 128:
        paddle_rect[0]+=0.3 * dt
    elif pressed[K_SPACE]:
        BALL_SERVED = True


    #If the ball touch a paddle, hit the ball back
    if paddle_rect[0] + paddle_rect.width >= ball_rect[0] >= paddle_rect[0] and \
        ball_rect[1] + ball_rect.height >= paddle_rect[1] and sy > 0:
        sy *= -1
        sx *= 1.02 #increase x speeed
        sy *= 1.02 #increase y speed
        continue

    #Destroy bricks
    DELETE_BRICK = None
    for b in bricks:
        bx, by = b
        if bx <= ball_rect[0] <= bx + brick_rect.width and \
        by <= ball_rect[1] <= by + brick_rect.height:
            DELETE_BRICK = b

    if DELETE_BRICK:
        bricks.remove(DELETE_BRICK)
        sy *= -1

    #Change movement direction if hit the end of the available height and width

    #top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1

    #bottom
    elif ball_rect[1] >= 600 - 24:
        BALL_SERVED = False
        ball_rect.topleft = ball_start

    #left
    elif ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx  *= -1

    #right
    elif ball_rect[0] >= 800 - 24:
        ball_rect[0] = 800 - 24
        sx *= -1

    #If True than move the ball
    if BALL_SERVED:
        ball_rect[0] += sx
        ball_rect[1] += sy

    #Correct exit if user press on quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    screen.fill((0,0,0))
