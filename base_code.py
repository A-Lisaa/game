#!/usr/bin/python3
#-*- coding: utf-8 -*-

import ctypes
import sys
import pygame
from pygame.locals import *
from map_drawer import map_drawer
from text import text

pygame.init()
pygame.mixer.init()

FPS = 60
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(1)

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID()
pygame.display.set_caption('Game')
pygame.display.set_icon(pygame.image.load("images/icon.ico"))

clock = pygame.time.Clock()
scr = pygame.display.set_mode((0, 0), FULLSCREEN)

game_run = True

while game_run:
    clock.tick(FPS)
    map_drawer(scr, "maps/map0.xml")
    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            game_run = False

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
sys.exit()