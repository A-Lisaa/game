#!/usr/bin/python3
#-*- coding: utf-8 -*-
import functions
import pygame
import actor_class
from map_drawer import get_map
from pygame.locals import *
from _init_settings import *
from characters import *

pygame.init()
pygame.mixer.init()

class Level:
    def __init__(self, map: str, characters: pygame.sprite.Group, actor: actor_class.Actor):
        self.scr = pygame.display.set_mode((int(screen_width), int(screen_height)), FULLSCREEN if eval(fullscreen) else None)
        self.map_surf, self.map_objects = get_map(map)
        
        self.characters = characters
        self.actor = actor
        
        self.keys = []
        self.shift = (0, 0)
        self.map_position = [0, 0]
    
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                functions.quit()
            if event.type == KEYDOWN:
                event.key = pygame.key.name(event.key)
                if event.key == pause:
                    functions.quit()
                self.keys.append(event.key)
            if event.type == KEYUP:
                self.keys.remove(pygame.key.name(event.key))
    
    def collision(self):
        print(self.actor.character.rect)
    
    def draw(self):
        self.scr.fill((0, 0, 0))
        self.scr.blit(self.map_surf, self.map_position)
        self.characters.update(self.shift)
        self.shift = (0, 0)
        self.characters.clear(self.scr, self.scr)
        self.characters.draw(self.scr)
    
    def run(self):
        while True:
            self.event_loop()
            self.draw()
                    
            pygame.display.update()
            pygame.display.flip()
            
if __name__ == "__main__":
    level0 = Level("test.tmx", chars, actor_class.Actor(sammy))
    level0.run()