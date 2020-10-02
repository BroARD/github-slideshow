import pygame
from Settings import *
import os
from math import *
from pygame.math import Vector2

pygame.init()

#MOVING
right = False
left = False
speed = 10.0
move_x = 960.0
move_y = 540.0
K_W = False
K_S = False

#RESOLUTION
SCREEN_WIDTN = 1920
SCREEN_HEIGHT = 1080



FPS = 60
clock = pygame.time.Clock()

sc = pygame.display.set_mode([SCREEN_WIDTN, SCREEN_HEIGHT], pygame.FULLSCREEN)
sc.fill(WHITE)
running = True

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')
player_image = pygame.image.load(os.path.join(image_path, 'body.png'))
player_rect = player_image.get_rect()
image_copy = player_image.copy()

angle = 0.0

circle = pygame.draw.ellipse(sc, GREEN, (200, 100, 1500, 800), 180)

while running:
    #body hero

    if right == True:
        player_image = pygame.transform.rotozoom(image_copy, angle, 1)
        sc.blit(player_image, Vector2(move_x, move_y))
        angle -= 2.0
    if left == True:
        player_image = pygame.transform.rotozoom(image_copy, angle, 1)
        sc.blit(player_image, Vector2(move_x, move_y))
        angle += 2.0
    if K_W == True:
        move_x = move_x - speed * cos(radians(180 - angle))  # для езды вперед
        move_y = move_y - speed * sin(radians(180 - angle))
    if K_S == True:
        move_x = move_x + speed * cos(radians(180 - angle))  # для езды вперед
        move_y = move_y + speed * sin(radians(180 - angle))
    pygame.display.flip()
    sc.fill(WHITE)

    clock.tick(FPS)
    #all KEY
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                K_W = True
            if event.key == pygame.K_s:
                K_S = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_w:
                K_W = False
            if event.key == pygame.K_s:
                K_S = False
            if event.key == pygame.K_d:
                right = False
        elif event.type == pygame.QUIT:
            exit()
    sc.blit(player_image, (move_x, move_y))

