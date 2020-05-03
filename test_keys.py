#!/usr/bin/python3
#-*- coding: utf-8 -*-

import ctypes
import sys
import os
import pygame
from pygame.locals import *
from map_drawer import *
from text import *
from set_settings import *

pygame.init()
pygame.mixer.init()

if not os.path.exists("settings.ini"):
    update_setting("Input", "exit", str(f"{K_ESCAPE} # escape"))
    update_setting("Input", "move_forward", str(f"{K_w} # w"))
    update_setting("Input", "move_backward", str(f"{K_s} # s"))
    update_setting("Input", "move_leftward", str(f"{K_a} # a"))
    update_setting("Input", "move_rightward", str(f"{K_d} # d"))

FPS = 60
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(1)

input = {"exit": get_key("Input", "exit"),
         "forward": get_key("Input", "move_forward"),
         "backward": get_key("Input", "move_backward"),
         "leftward": get_key("Input", "move_leftward"),
         "rightward": get_key("Input", "move_rightward")}
position = (SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2)
start_position = position
x_pos = start_position[0] - position[0]
y_pos = start_position[1] - position[1]
step = 16
size_of_characters = (16, 16)
actor_image = "images/samantha_back.png"

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID()
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load("images/icon.ico"))

clock = pygame.time.Clock()
scr = pygame.display.set_mode((0, 0), FULLSCREEN)

map_drawer(scr, "maps/map0.xml")

all_characters = pygame.sprite.Group()

class Character(pygame.sprite.Sprite):
    def __init__(self, actor_image_filename, group, position_of_actor, size_of_characters = size_of_characters):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(actor_image_filename), size_of_characters)
        self.rect = self.image.get_rect(center = position_of_actor)
        self.add(group)

    def update(self, actor_image_filename, new_position, old_position, step = step, size_of_characters = size_of_characters):
        if old_position[0] < new_position[0]:
            self.rect.x -= step
        elif old_position[0] > new_position[0]:
            self.rect.x += step
        if old_position[1] < new_position[1]:
            self.rect.y -= step
        elif old_position[1] > new_position[1]:
            self.rect.y += step
        self.image = pygame.transform.scale(pygame.image.load(actor_image_filename), size_of_characters)

class Actor:
    def __init__(self, actor_image_filename, size_of_actor = size_of_characters):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(actor_image_filename), size_of_actor)
        self.rect = self.image.get_rect(topleft = (SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2))

    def update(self, actor_image_filename, size_of_actor = size_of_characters):
        self.image = pygame.transform.scale(pygame.image.load(actor_image_filename), size_of_actor)

actor = Actor(actor_image)
character = Character(actor_image, all_characters, (1000, 650))

def calculation_position(direction, position, step = step, actor_image = actor_image):
    (x, y) = position
    if direction == input["leftward"]:
        x -= step
        actor_image = "images/samantha_left.png"
    elif direction == input["rightward"]:
        x += step
        actor_image = "images/samantha_right.png"
    if direction == input["forward"]:
        y -= step
        actor_image = "images/samantha_left.png" # forward
    elif direction == input["backward"]:
        y += step
        actor_image = "images/samantha_back.png"
    return actor_image, (x, y)

scr.blit(actor.image, actor.rect)
all_characters.draw(scr)

move = False
menu = False
game_run = True

while game_run:
    clock.tick(FPS)
    if menu:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_c:
                    menu = False
                else:
                    update_setting("Input", "move_forward", str(f"{event.key} # {pygame.key.name(event.key)}"))
    else:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_run = False
            if event.type == KEYDOWN:
                if event.key == input["exit"]:
                    game_run = False
                direction = event.key
                move = True
            if event.type == KEYUP:
                move = False

        map_drawer(scr, "maps/map0.xml", x_pos, y_pos)
        scr.blit(actor.image, actor.rect)
        all_characters.draw(scr)

        if move:
            old_position = position
            result = calculation_position(direction, position)
            actor_image = result[0]
            position = result[1]
            x_pos = start_position[0] - position[0]
            y_pos = start_position[1] - position[1]
            actor.update(actor_image)
            all_characters.update(actor_image, position, old_position)
            text(scr, "Alice", "You're walking")
        else:
            text(scr, "Alice", "You've stopped")

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
sys.exit()