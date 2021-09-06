import pygame
from _init_settings import *
from character_class import Character
pygame.init()

class Actor(Character):
    def __init__(self, character: Character):
        self.character = character
        
    def move(self, keys):
        if keys:
            key = keys[-1]
            speed = self.character.speed
            if sprint in keys:
                speed *= int(sprint_modifier)
                try:
                    for iter_key in keys[::-1]:
                        if iter_key in (move_leftward, move_rightward, move_forward, move_backward):
                            key = iter_key
                except Exception:
                    pass
            if key in move_leftward:
                map_position[0] += speed
                shift = (+speed, 0)
                self.character.image = self.character.character_image_leftward
            elif key in move_rightward:
                map_position[0] -= speed
                shift = (-speed, 0)
                self.character.image = self.character.character_image_rightward
            elif key in move_forward:
                map_position[1] += speed
                shift = (0, +speed)
                self.character.image = self.character.character_image_forward
            elif key in move_backward:
                map_position[1] -= speed
                shift = (0, -speed)
                self.character.image = self.character.character_image_backward