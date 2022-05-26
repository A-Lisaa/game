#!/usr/bin/python3
#-*- coding: utf-8 -*-

## Ввод с клавиатуры
#string = ""
#if pygame.key.name(event.key) in alphabet or pygame.key.name(event.key) == "space":
#    if pygame.key.name(event.key) == "space":
#        letter = " "
#    elif pygame.key.name(event.key) != "space":
#        letter = pygame.key.name(event.key)
#        if pygame.key.get_mods() == KMOD_LSHIFT or KMOD_RSHIFT:
#            letter = letter.upper()
#    string += letter
import __init__
import ctypes
import sys
import os
import pygame
from pygame.locals import *
from map_drawer import get_map
from text import text
from music import bg_music
from buttons import Text_Button
from default_settings import set_default_settings
from __init_settings__ import *

pygame.init()
pygame.mixer.init()

input_keys = {}

if not os.path.exists("settings.ini"):
    set_default_settings()

fps = int(fps)
screen_height = int(screen_height)
screen_width = int(screen_width)

position = (screen_height / 2, screen_width / 2)
start_position = position
x_pos = start_position[0] - position[0]
y_pos = start_position[1] - position[1]
menu_color = (0, 255, 255) # циановый
actor_image = "images/samantha_back.png"

alphabet = ('1234567890abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя')

pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load("icon.ico"))

clock = pygame.time.Clock()
scr = pygame.display.set_mode((0, 0), FULLSCREEN)

main_menu_screen = pygame.Surface((screen_height, screen_width), SRCALPHA)
pause_screen = pygame.Surface((screen_height, screen_width), SRCALPHA)
settings_screen = pygame.Surface((screen_height, screen_width), SRCALPHA)

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

def calculation_position(direction, position, step = int(size), actor_image = actor_image):
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

def change_button(button_name, alphabet = alphabet):
    wait_for_key = True
    text(scr, "", "Нажмите клавишу, на которую изменить")
    pygame.display.update()
    while wait_for_key:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key not in input_keys.values():
                    update_setting("Input", button_name, f"{event.key} # {pygame.key.name(event.key)}")
                    exec(f"{button_name} = {event.key}")
                elif event.key in input_keys.values():
                    for key, value in input_keys.items():
                        if value == event.key:
                            update_setting("Input", key, f"{input_keys[button_name]} # {pygame.key.name(input_keys[button_name])}")
                            update_setting("Input", button_name, f"{input_keys[key]} # {pygame.key.name(input_keys[key])}")
                            input_keys[key], input_keys[button_name] = input_keys[button_name], input_keys[key]
                wait_for_key = False

move = False

main_menu = True
settings = False
pause = False
game = False

main_cycle = True

bg_music("music/chapter_four.mp3")
pygame.mixer.music.pause()

while main_cycle:
    clock.tick(fps)
    if main_menu:
        scr.blit(main_menu_screen, (0, 0))
        main_menu_screen.fill(menu_color)
        new_game_button.create_button(main_menu_screen, "Начать игру", screen_height / 2 - 200 / 2, screen_width / 2 - 250, 200, 100)
        settings_button.create_button(main_menu_screen, "Настройки", screen_height / 2 - 200 / 2, screen_width / 2 - 125, 200, 100)
        quit_button.create_button(main_menu_screen, "Выход", screen_height / 2 - 200 / 2, screen_width / 2, 200, 100)
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
        change_move_forward_button.create_button(settings_screen, f"Вперед ({pygame.key.name(input_keys['move_forward'])})", screen_height / 2 - 200 / 2, screen_width / 2 - 500, 200, 100)
        change_move_backward_button.create_button(settings_screen, f"Назад ({pygame.key.name(input_keys['move_backward'])})", screen_height / 2 - 200 / 2, screen_width / 2 - 375, 200, 100)
        change_move_leftward_button.create_button(settings_screen, f"Влево ({pygame.key.name(input_keys['move_leftward'])})", screen_height / 2 - 200 / 2, screen_width / 2 - 250, 200, 100)
        change_move_rightward_button.create_button(settings_screen, f"Вправо ({pygame.key.name(input_keys['move_rightward'])})", screen_height / 2 - 200 / 2, screen_width / 2 - 125, 200, 100)
        change_pause_button.create_button(settings_screen, f"Пауза ({pygame.key.name(input_keys['pause'])})", screen_height / 2 - 200 / 2, screen_width / 2, 200, 100)
        default_button.create_button(settings_screen, "По умолчанию", screen_height - 225, screen_width - 250, 200, 100)
        main_menu_button.create_button(settings_screen, "В главное меню", screen_height - 225, screen_width - 125, 200, 100)
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
                    set_default_settings()
                if main_menu_button.pressed(pygame.mouse.get_pos()):
                    settings = False
                    main_menu = True
    elif pause:
        scr.blit(pause_screen, (0, 0))
        pause_screen.fill(menu_color)
        resume_game_button.create_button(pause_screen, "Продолжить игру", screen_height / 2 - 200 / 2, screen_width / 2 - 250, 200, 100)
        main_menu_button.create_button(pause_screen, "В главное меню", screen_height / 2 - 200 / 2, screen_width / 2 - 125, 200, 100)
        quit_button.create_button(pause_screen, "Выход", screen_height / 2 - 200 / 2, screen_width / 2, 200, 100)
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
        pygame.mixer.music.unpause()
        for event in pygame.event.get():
            if event.type == QUIT:
                main_cycle = False
            if event.type == KEYDOWN:
                if event.key == input_keys["pause"]:
                    game = False
                    pause = True
                    pygame.mixer.music.pause()
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