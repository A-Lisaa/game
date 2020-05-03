#!/usr/bin/python3
#-*- coding: utf-8 -*-

import ctypes
import sys
import os
import pygame
from pygame.locals import *
from map_drawer import *
from text import *
from music import *
from buttons import *
from set_settings import *

pygame.init()
pygame.mixer.init()

if not os.path.exists("settings.ini"):
    update_setting("Input", "pause", str(f"{K_ESCAPE} # escape"))
    update_setting("Input", "move_forward", str(f"{K_w} # w"))
    update_setting("Input", "move_backward", str(f"{K_s} # s"))
    update_setting("Input", "move_leftward", str(f"{K_a} # a"))
    update_setting("Input", "move_rightward", str(f"{K_d} # d"))

FPS = 60
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(1)

input = {"pause": get_key("Input", "pause"),
         "move_forward": get_key("Input", "move_forward"),
         "move_backward": get_key("Input", "move_backward"),
         "move_leftward": get_key("Input", "move_leftward"),
         "move_rightward": get_key("Input", "move_rightward")}
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
menu_screen = pygame.Surface((SCREEN_HEIGHT, SCREEN_WIDTH), SRCALPHA)
pause_screen = pygame.Surface((SCREEN_HEIGHT, SCREEN_WIDTH), SRCALPHA)

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
new_game_button = Text_Button()
settings_button = Text_Button()
quit_button = Text_Button()
resume_game_button = Text_Button()

def calculation_position(direction, position, step = step, actor_image = actor_image):
    (x, y) = position
    if direction == input["move_leftward"]:
        x -= step
        actor_image = "images/samantha_left.png"
    elif direction == input["move_rightward"]:
        x += step
        actor_image = "images/samantha_right.png"
    if direction == input["move_forward"]:
        y -= step
        actor_image = "images/samantha_left.png" # forward
    elif direction == input["move_backward"]:
        y += step
        actor_image = "images/samantha_back.png"
    return actor_image, (x, y)

move = False

menu = True
settings = False
pause = False
game = False

main_cycle = True

bg_music("music/chapter_four.mp3")

while main_cycle:
    clock.tick(FPS)
    if menu:
        scr.blit(menu_screen, (0, 0))
        menu_screen.fill((0, 255, 255))
        new_game_button.create_button(menu_screen, "Начать игру", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 250, 200, 100)
        settings_button.create_button(menu_screen, "Настройки", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 125, 200, 100)
        quit_button.create_button(menu_screen, "Выход", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2, 200, 100)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if new_game_button.pressed(pygame.mouse.get_pos()):
                    menu = False
                    game = True
                if settings_button.pressed(pygame.mouse.get_pos()):
                    pass
                if quit_button.pressed(pygame.mouse.get_pos()):
                    main_cycle = False
    elif settings:
        pass
        #update_setting("Input", "move_forward", str(f"{event.key} # {pygame.key.name(event.key)}"))
        #settings = False
    elif pause:
        scr.blit(pause_screen, (0, 0))
        pause_screen.fill((0, 255, 255))
        resume_game_button.create_button(pause_screen, "Продолжить игру", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 250, 200, 100)
        settings_button.create_button(pause_screen, "Настройки", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 125, 200, 100)
        quit_button.create_button(pause_screen, "Выход", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2, 200, 100)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == input["pause"]:
                    pause = False
                    game = True
            if event.type == MOUSEBUTTONDOWN:
                if resume_game_button.pressed(pygame.mouse.get_pos()):
                    pause = False
                    game = True
                if settings_button.pressed(pygame.mouse.get_pos()):
                    pass
                if quit_button.pressed(pygame.mouse.get_pos()):
                    main_cycle = False
    elif game:
        for event in pygame.event.get():
            if event.type == QUIT:
                main_cycle = False
            if event.type == KEYDOWN:
                if event.key == input["pause"]:
                    game = False
                    pause = True
                elif event.key in (input["move_forward"], input["move_backward"], input["move_leftward"], input["move_rightward"]):
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
            if pygame.sprite.spritecollideany(actor, all_characters):
                bg_music("music/afterlife.mp3")
            actor.update(actor_image)
            all_characters.update(actor_image, position, old_position)
            text(scr, "Alice", "You're walking")
        else:
            text(scr, "Alice", "You've stopped")

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
sys.exit()