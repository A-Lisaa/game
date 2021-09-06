import pygame
from logger import get_logger
from _init_settings import *
from pygame.locals import *


class Character(pygame.sprite.Sprite):
    def __init__(self, name: str, character_image_file: str, character_position: tuple, color=(255, 165, 0), start_direction: str = "backward"):
        log = get_logger(__file__)
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.color = color
        self.speed = 1

        # ? How walk gif should work? For every step - one gif stage, where step, let's say, 20px? Gif frame changes every n millisecons?
        self.character_image_forward = pygame.image.load(
            f"{characters_path}\\{character_image_file}_forward.png")
        self.character_image_backward = pygame.image.load(
            f"{characters_path}\\{character_image_file}_backward.png")
        self.character_image_leftward = pygame.image.load(
            f"{characters_path}\\{character_image_file}_leftward.png")
        self.character_image_rightward = pygame.image.load(
            f"{characters_path}\\{character_image_file}_rightward.png")
        exec(f"self.image = self.character_image_{start_direction}")
        self.rect = self.image.get_rect(center=character_position)

        log.debug(f"Character {name} created")

    def update(self, shift: tuple):
        # Character.rect shows the position of sprite, should change it
        self.rect.x = self.rect.x+shift[0]
        # Character is drawn by Group.draw, Group.draw uses Character.rect from Sprite
        self.rect.y = self.rect.y+shift[1]


if __name__ == "__main__":
    pygame.init()
    scr = pygame.display.set_mode((800, 600))

    actors = pygame.sprite.Group()
    npcs = pygame.sprite.Group()

    actor = Character("Samantha", "samantha", (400, 300))
    actors.add(actor)
    npc0 = Character("Npc0", "samantha", (200, 100))
    npcs.add(npc0)

    keys = []
    bg = pygame.Surface((800, 600))
    while True:
        pygame.time.Clock().tick(int(fps))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                keys.append(pygame.key.name(event.key))
            if event.type == KEYUP:
                keys.remove(pygame.key.name(event.key))
        if keys:
            key = keys[-1]
            speed = actor.speed
            if sprint in keys:
                speed *= float(sprint_modifier)
                try:
                    for iter_key in keys[::-1]:
                        if iter_key in (move_leftward, move_rightward, move_forward, move_backward):
                            key = iter_key
                except Exception:
                    pass
            if key in move_leftward:
                actor.rect.x -= speed
                actor.image = actor.character_image_leftward
            elif key in move_rightward:
                actor.rect.x += speed
                actor.image = actor.character_image_rightward
            elif key in move_forward:
                actor.rect.y -= speed
                actor.image = actor.character_image_forward
            elif key in move_backward:
                actor.rect.y += speed
                actor.image = actor.character_image_backward

        actors.clear(scr, bg)
        npcs.clear(scr, bg)
        actors.draw(scr)
        npcs.draw(scr)

        pygame.display.update()
        pygame.display.flip()
