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

input_keys = {}

def default_settings():
    update_setting("Input", "pause", str(f"{K_ESCAPE} # {pygame.key.name(K_ESCAPE)}"))
    update_setting("Input", "move_forward", str(f"{K_w} # {pygame.key.name(K_w)}"))
    update_setting("Input", "move_backward", str(f"{K_s} # {pygame.key.name(K_s)}"))
    update_setting("Input", "move_leftward", str(f"{K_a} # {pygame.key.name(K_a)}"))
    update_setting("Input", "move_rightward", str(f"{K_d} # {pygame.key.name(K_d)}"))
    get_all_keys_from_section(input_keys)

if not os.path.exists("settings.ini"):
    default_settings()

get_all_keys_from_section(input_keys)

FPS = 60
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(1)

position = (SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2)
start_position = position
x_pos = start_position[0] - position[0]
y_pos = start_position[1] - position[1]
step = 16
size_of_characters = (16, 16)
menu_color = (0, 255, 255) # циановый
actor_image = "images/samantha_back.png"

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID()
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load("images/icon.ico"))

clock = pygame.time.Clock()
scr = pygame.display.set_mode((0, 0), FULLSCREEN)

main_menu_screen = pygame.Surface((SCREEN_HEIGHT, SCREEN_WIDTH), SRCALPHA)
pause_screen = pygame.Surface((SCREEN_HEIGHT, SCREEN_WIDTH), SRCALPHA)
settings_screen = pygame.Surface((SCREEN_HEIGHT, SCREEN_WIDTH), SRCALPHA)

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
pause_button = Text_Button()
main_menu_button = Text_Button()
default_button = Text_Button()

change_move_forward_button = Text_Button()
change_move_backward_button = Text_Button()
change_move_leftward_button = Text_Button()
change_move_rightward_button = Text_Button()
change_pause_button = Text_Button()

def calculation_position(direction, position, step = step, actor_image = actor_image):
    (x, y) = position
    if direction == input_keys["move_leftward"]:
        x -= step
        actor_image = "images/samantha_left.png"
    elif direction == input_keys["move_rightward"]:
        x += step
        actor_image = "images/samantha_right.png"
    if direction == input_keys["move_forward"]:
        y -= step
        actor_image = "images/samantha_forward.png"
    elif direction == input_keys["move_backward"]:
        y += step
        actor_image = "images/samantha_back.png"
    return actor_image, (x, y)

def change_button(button_name):
    wait_for_key = True
    while wait_for_key:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                update_setting("Input", button_name, str(f"{event.key} # {pygame.key.name(event.key)}"))
                input_keys[button_name] = event.key
                wait_for_key = False

move = False

main_menu = True
settings = False
pause = False
game = False

main_cycle = True

bg_music("music/chapter_four.mp3")

while main_cycle:
    clock.tick(FPS)
    if main_menu:
        scr.blit(main_menu_screen, (0, 0))
        main_menu_screen.fill(menu_color)
        new_game_button.create_button(main_menu_screen, "Начать игру", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 250, 200, 100)
        settings_button.create_button(main_menu_screen, "Настройки", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 125, 200, 100)
        quit_button.create_button(main_menu_screen, "Выход", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2, 200, 100)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if new_game_button.pressed(pygame.mouse.get_pos()):
                    main_menu = False
                    game = True
                if settings_button.pressed(pygame.mouse.get_pos()):
                    main_menu = False
                    settings = True
                if quit_button.pressed(pygame.mouse.get_pos()):
                    main_cycle = False
    elif settings:
        scr.blit(settings_screen, (0, 0))
        settings_screen.fill(menu_color)
        change_move_forward_button.create_button(settings_screen, f"Вперед ({pygame.key.name(input_keys['move_forward'])})", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 500, 200, 100)
        change_move_backward_button.create_button(settings_screen, f"Назад ({pygame.key.name(input_keys['move_backward'])})", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 375, 200, 100)
        change_move_leftward_button.create_button(settings_screen, f"Влево ({pygame.key.name(input_keys['move_leftward'])})", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 250, 200, 100)
        change_move_rightward_button.create_button(settings_screen, f"Вправо ({pygame.key.name(input_keys['move_rightward'])})", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 125, 200, 100)
        change_pause_button.create_button(settings_screen, f"Пауза ({pygame.key.name(input_keys['pause'])})", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2, 200, 100)
        default_button.create_button(settings_screen, "По умолчанию", SCREEN_HEIGHT - 225, SCREEN_WIDTH - 250, 200, 100)
        main_menu_button.create_button(settings_screen, "В главное меню", SCREEN_HEIGHT - 225, SCREEN_WIDTH - 125, 200, 100)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if change_move_forward_button.pressed(pygame.mouse.get_pos()):
                    change_button("move_forward")
                if change_move_backward_button.pressed(pygame.mouse.get_pos()):
                    change_button("move_backward")
                if change_move_leftward_button.pressed(pygame.mouse.get_pos()):
                    change_button("move_leftward")
                if change_move_rightward_button.pressed(pygame.mouse.get_pos()):
                    change_button("move_rightward")
                if change_pause_button.pressed(pygame.mouse.get_pos()):
                    change_button("pause")
                if default_button.pressed(pygame.mouse.get_pos()):
                    default_settings()
                if main_menu_button.pressed(pygame.mouse.get_pos()):
                    settings = False
                    main_menu = True
    elif pause:
        scr.blit(pause_screen, (0, 0))
        pause_screen.fill(menu_color)
        resume_game_button.create_button(pause_screen, "Продолжить игру", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 250, 200, 100)
        main_menu_button.create_button(pause_screen, "В главное меню", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2 - 125, 200, 100)
        quit_button.create_button(pause_screen, "Выход", SCREEN_HEIGHT / 2 - 200 / 2, SCREEN_WIDTH / 2, 200, 100)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == input_keys["pause"]:
                    pause = False
                    game = True
            if event.type == MOUSEBUTTONDOWN:
                if resume_game_button.pressed(pygame.mouse.get_pos()):
                    pause = False
                    game = True
                if main_menu_button.pressed(pygame.mouse.get_pos()):
                    pause = False
                    main_menu = True
                if quit_button.pressed(pygame.mouse.get_pos()):
                    main_cycle = False
    elif game:
        for event in pygame.event.get():
            if event.type == QUIT:
                main_cycle = False
            if event.type == KEYDOWN:
                if event.key == input_keys["pause"]:
                    game = False
                    pause = True
                elif event.key in (input_keys["move_forward"], input_keys["move_backward"], input_keys["move_leftward"], input_keys["move_rightward"]):
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