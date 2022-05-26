import __init__
import os
import pygame
from __init_settings__ import settings
from typing import Union

class Gif:
    def __init__(self, pics: Union[str, list, tuple]):
        if type(pics) == str:
            pics = f'{settings["images_path"]}\\{pics}'
            if os.path.exists(pics):
                pics = ("\\".join((pics, frame)).replace("\\", "\\\\") for frame in os.listdir(pics))
            else:
                raise OSError("Path does not exist")
        elif type(pics) in (list, tuple):
            pass
        else:
            raise ValueError("Invalid pics argument, should be path to a folder containing pictures or list/tuple with pygame.")

        self.pictures = []
        for frame in pics:
            self.pictures.append(pygame.image.load(frame))
    
    def play_gif(self, delay = 0.1):
        surface = pygame.Surface((100, 100))
        for frame in self.pictures:
            surface.blit(frame, (0, 0, 0, 0))
    
if __name__ == "__main__":
    gif = Gif("characters\\test-character")
    gif.play_gif()