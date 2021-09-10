#!/usr/bin/python3
#-*- coding: utf-8 -*-
import pygame
from pygame.locals import *

def text(screen, name, phrase, color_of_phrase = (255, 255, 255), color_of_name = (255, 255, 255), smooth = 1, alpha = 150):
    bg = pygame.Surface((1920, 230), SRCALPHA)
    bg.fill((150, 0, 0, alpha))
    font = pygame.font.SysFont(None, 36)
    say = font.render(phrase, smooth, color_of_phrase)
    name = font.render(name, smooth, color_of_name)
    screen.blit(bg, (0, 850))
    pygame.draw.line(screen, (0, 150, 0), (0, 890), (1920, 890))
    screen.blit(name, (10, 860))
    screen.blit(say, (10, 900))