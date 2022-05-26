import pygame

from __init_settings__ import settings
from character_class import Character

pygame.init()

class Actor:
    def __init__(self, character: Character):
        self.character = character

    def move(self, keys):
        if keys:
            key = keys[-1]
            speed = self.character.speed
            if settings["sprint"] in keys:
                speed *= int(settings["sprint_modifier"])
                for iter_key in keys[::-1]:
                    if iter_key in (settings["move_leftward"], settings["move_rightward"],
                                    settings["move_forward"], settings["move_backward"]):
                        key = iter_key
            if key in settings["move_leftward"]:
                map_position = (+speed, 0)
                shift = (+speed, 0)
                self.character.image = self.character.character_image_leftward
            elif key in settings["move_rightward"]:
                map_position = (-speed, 0)
                shift = (-speed, 0)
                self.character.image = self.character.character_image_rightward
            elif key in settings["move_forward"]:
                map_position = (0, +speed)
                shift = (0, +speed)
                self.character.image = self.character.character_image_forward
            elif key in settings["move_backward"]:
                map_position = (0, -speed)
                shift = (0, -speed)
                self.character.image = self.character.character_image_backward
