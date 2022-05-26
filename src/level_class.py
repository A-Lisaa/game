#!/usr/bin/python3
#-*- coding: utf-8 -*-
import __init__
import pygame
import actor_class
import UF
from map_drawer import get_map
from pygame.locals import *
from __init_settings__ import *
from characters import *

pygame.init()
pygame.mixer.init()

class Level:
    """
    Class of every location in game, consists of objects that can exist w/o Actor:
    Map; Mask of map; Characters; Events
    """
    def __init__(self, map: str, characters: pygame.sprite.Group):
        if eval(settings["fullscreen"]):
            self.scr = pygame.display.set_mode((int(settings["screen_width"]), int(settings["screen_height"])), FULLSCREEN)
        else:
            self.scr = pygame.display.set_mode((int(settings["screen_width"]), int(settings["screen_height"])))
        self.map_surf, self.map_objects = get_map(map)
        
        self.characters = characters
        
        self.shift = (0, 0)
        self.map_position = [0, 0]
    
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                UF.quit()
            if event.type == KEYDOWN:
                event.key = pygame.key.name(event.key)
                if event.key == settings["pause"]:
                    UF.quit()
                self.keys.append(event.key)
            if event.type == KEYUP:
                self.keys.remove(pygame.key.name(event.key))
    
    def draw(self):
        self.scr.fill((0, 0, 0))
        self.scr.blit(self.map_surf, self.map_position)
        self.characters.update(self.shift)
        self.shift = (0, 0)
        self.characters.clear(self.scr, self.scr)
        self.characters.draw(self.scr)
    
    def run(self):
        self.event_loop()
        self.draw()
                
        pygame.display.update()
        pygame.display.flip()
            
if __name__ == "__main__":
    level0 = Level("test.tmx", chars)
    while True:
        level0.run()