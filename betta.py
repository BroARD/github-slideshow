import pygame
from Settings import *
import os
import math

pygame.init()

#MOVING
up = False
down = False
right = False
left = False
speed = 10
speed_test = False
move_x = 200
move_y = 200


#RESOLUTION
SCREEN_WIDTN = 1920
SCREEN_HEIGHT = 1080



coordination_x = SCREEN_WIDTN//2
coordination_y = SCREEN_HEIGHT//2
FPS = 60
clock = pygame.time.Clock()

sc = pygame.display.set_mode([SCREEN_WIDTN, SCREEN_HEIGHT], pygame.FULLSCREEN)
sc.fill(WHITE)
running = True

current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'images') # The image folder path

player_image = pygame.image.load(os.path.join(image_path, 'body.png'))
image_copy = player_image.copy()
angle = 0

rect = player_image.get_rect(center=(move_x, move_y))

while running:
    #body hero
    sc.blit(player_image, (move_x, move_y))
    if speed_test == True and speed < 30:
        speed+=speed
    if speed_test == False and speed >= 25:
        speed-=speed
    if right == True:
        player_image = pygame.transform.rotozoom(image_copy, angle, 1)
        sc.blit(player_image, (move_x, move_y))
        angle -= 10
    if left == True:
        player_image = pygame.transform.rotozoom(image_copy, angle, 1)
        sc.blit(player_image, (move_x, move_y))
        angle += 10
    if up == True:
        move_x += speed
    if down == True:
        move_x -= speed

    pygame.display.flip()
    sc.fill(WHITE)

    clock.tick(FPS)
    #all KEY
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_SPACE:
                speed_test = True
                print('da')
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                speed_test = False
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_s:
                down = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
        elif event.type == pygame.QUIT:
            exit()
