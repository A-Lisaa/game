#!/usr/bin/python3
#-*- coding: utf-8 -*-
import pygame
import actor_class
from functions import UF
from map_drawer import get_map
from pygame.locals import *
from _init_settings import *
from characters import *

pygame.init()
pygame.mixer.init()

class Game:
    def __init__(self):
        self.scr = pygame.display.set_mode((0, 0), FULLSCREEN)
        self.map_surf, self.map_objects = get_map("test.tmx")
        
        self.keys = []
        self.shift = (0, 0)
        self.map_position = [0, 0]
        
        self.actor = actor_class.Actor(sammy)
    
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                UF.game_quit()
            if event.type == KEYDOWN:
                event.key = pygame.key.name(event.key)
                if event.key == pause:
                    UF.game_quit()
                self.keys.append(event.key)
            if event.type == KEYUP:
                self.keys.remove(pygame.key.name(event.key))
    
    def collision(self):
        print(self.actor.character.rect)
    
    def draw(self):
        self.scr.fill((0, 0, 0))
        self.scr.blit(self.map_surf, self.map_position)
        chars.update(self.shift)
        self.shift = (0, 0)
        chars.clear(self.scr, self.scr)
        chars.draw(self.scr)
    
    def run(self):
        while True:
            self.event_loop()
            self.actor_move()
            self.draw()
                    
            pygame.display.update()
            pygame.display.flip()
            
if __name__ == "__main__":
    game = Game()
    game.run()