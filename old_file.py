#!/usr/bin/python3
#-*- coding: utf-8 -*-

import ctypes
import sys
import map_drawer
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
## Константы
BLACK = (0, 0, 0)
FPS = 60
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(1)

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID()
pygame.display.set_caption('Game')
pygame.display.set_icon(pygame.image.load("images/icon.ico"))

clock = pygame.time.Clock()
scr = pygame.display.set_mode((0, 0), FULLSCREEN)

borders = []

block_height = 50
block_width = 50
block_step = int(SCREEN_HEIGHT * SCREEN_WIDTH / 10 ** 6 * 5)
block_color = (0, 0, 255)
block_position_X = SCREEN_HEIGHT / 2 - block_height
block_position_Y = SCREEN_WIDTH / 2 - block_width
block_position = (block_position_X, block_position_Y)

direction = False
move = False
game_run = True

def new_position(dir_flag, pos):
    (x, y) = pos
    if dir_flag:
        if dir_flag == K_LEFT or dir_flag == K_a:
            x -= block_step
        elif dir_flag == K_RIGHT or dir_flag == K_d:
            x += block_step
        if dir_flag == K_UP or dir_flag == K_w:
            y -= block_step
        elif dir_flag == K_DOWN or dir_flag == K_s:
            y += block_step
    return (x, y)

while game_run:
    clock.tick(FPS)
    map_drawer.map_drawer(scr, "maps/map0.xml")
    block_rect = pygame.Rect(block_position, (block_width, block_height))
    block = pygame.draw.rect(scr, block_color, block_rect, 3)
    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            game_run = False
        if event.type == KEYDOWN:
            direction = event.key
            move = True
        if event.type == KEYUP:
            direction = False
            move = False
    saved_position = block_position
    block_position = new_position(direction, block_position)

    if move:
        for border in borders:
            testRect = pygame.Rect(block_position, (block_width, block_height))
            if testRect.colliderect(border[1]):
                if block_position[0] < saved_position[0]:
                    block_position = (saved_position[0] - (block_step + block_position[0] - (border[1][0] + border[1][2])), saved_position[1])
                elif block_position[0] > saved_position[0]:
                    block_position = (saved_position[0] + (block_step - (block_position[0] + block_height - border[1][0])), saved_position[1])
                if block_position[1] < saved_position[1]:
                    block_position = (saved_position[0], saved_position[1] - (block_step + block_position[1] - (border[1][1] + border[1][3])))
                elif block_position[1] > saved_position[1]:
                    block_position = (saved_position[0], saved_position[1] + (block_step - (block_position[1] + block_width - border[1][1])))

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
sys.exit()