import attr
import pygame
import pygame.locals

from __init_settings__ import settings
from class_effect import Effect
from class_item_equipment import ItemEquipment
from logger import get_logger
from class_storage import Storage
from list_item_equipment import default_head
from constants import *


@attr.s(hash=True)
class Character():
    # ! Everything with something mutable should be overloaded in __init__ of a child
    # Base info
    name: str = attr.ib()
    sprite_folder: str = attr.ib()
    color: tuple[int, int, int] = attr.ib(default=DEFAULT_COLOR)

    # Draw info
    position: tuple | list = attr.ib(default=DEFAULT_POSITION)
    direction: str = attr.ib(default=DEFAULT_DIRECTION)

    # Health stats
    isAlive: bool | int = attr.ib(default=True)
    health: float = attr.ib(default=DEFAULT_HEALTH)
    health_max: float = attr.ib(default=DEFAULT_HEALTH)
    poison: bool | int = attr.ib(default=False)

    # Equipment stats
    head_protection: float = attr.ib(default=0)
    body_protection: float = attr.ib(default=0)

    # ! Mutables
    effects: list[Effect] = attr.ib(factory=list[Effect])
    equipment: dict[str, ItemEquipment] = attr.ib(factory=dict[str, ItemEquipment])
    inventory: Storage = attr.ib(default=Storage())

    def __init__(self, *args, **kwargs):
        self.effects = []
        self.equipment = {}
        self.inventory = Storage()

    def equip(self, equipment_item: ItemEquipment):
        self.equipment[equipment_item.slot] = equipment_item
        for buff in equipment_item.buffs:
            setattr(self, buff.stat, getattr(self, buff.stat) + buff.strength)

    def unequip(self, equipment_item: ItemEquipment):
        self.equipment[equipment_item.slot] = eval(f"default_{equipment_item.slot}")
        for buff in equipment_item.buffs:
            setattr(self, buff.stat, getattr(self, buff.stat) - buff.strength)

    def add_effect(self, effect: Effect):
        if not effect in self.effects:
            self.effects.append(effect)

    def update(self):
        pass

# class Character(CharacterData, pygame.sprite.Sprite):
#     def __init__(self):
#         self.log = get_logger(__file__)
#         super().__init__()

#         self.money = {"gold": 0, # Use money dict ("money name": amount)
#                       "silver": 0
#                       }

#         # ? How walk gif should work? For every step - one gif stage, where step, let's say, 20px? Gif frame changes every n millisecons?
#         character_image_forward = pygame.image.load(f"{settings['characters_path']}\\{character_image_file}_forward.png")
#         character_image_backward = pygame.image.load(f"{settings['characters_path']}\\{character_image_file}_backward.png")
#         character_image_leftward = pygame.image.load(f"{settings['characters_path']}\\{character_image_file}_leftward.png")
#         character_image_rightward = pygame.image.load(f"{settings['characters_path']}\\{character_image_file}_rightward.png")
#         start_directions = {"forward":character_image_forward,
#                             "backward": character_image_backward,
#                             "leftward": character_image_leftward,
#                             "rightward": character_image_rightward}
#         self.image = start_directions[start_direction]
#         self.rect = self.image.get_rect(center=character_position)

#         log.debug("Character %s created", name)

#     def update(self, shift: tuple):
#         # Character.rect shows the position of sprite, should change it
#         self.rect.x = self.rect.x+shift[0]
#         # Character is drawn by Group.draw, Group.draw uses Character.rect from Sprite
#         self.rect.y = self.rect.y+shift[1]


# if __name__ == "__main__":
    # pygame.init()
    # scr = pygame.display.set_mode((800, 600))

    # actors = pygame.sprite.Group()
    # npcs = pygame.sprite.Group()

    # actor = Character("Samantha", "samantha", (400, 300))
    # actors.add(actor)
    # npc0 = Character("Npc0", "samantha", (200, 100))
    # npcs.add(npc0)

    # keys = []
    # bg = pygame.Surface((800, 600))
    # while True:
    #     pygame.time.Clock().tick(int(settings["fps"]))
    #     for event in pygame.event.get():
    #         if event.type == pygame.locals.KEYDOWN:
    #             keys.append(pygame.key.name(event.key))
    #         if event.type == pygame.locals.KEYUP:
    #             keys.remove(pygame.key.name(event.key))
    #     if keys:
    #         key = keys[-1]
    #         speed = actor.speed
    #         if settings["sprint"] in keys:
    #             speed *= float(settings["sprint_modifier"])
    #             for iter_key in keys[::-1]:
    #                 if iter_key in (settings["move_leftward"], settings["move_rightward"],
    #                                 settings["move_forward"], settings["move_backward"]):
    #                     key = iter_key
    #         if key in settings["move_leftward"]:
    #             actor.rect.x -= speed
    #             actor.image = actor.character_image_leftward
    #         elif key in settings["move_rightward"]:
    #             actor.rect.x += speed
    #             actor.image = actor.character_image_rightward
    #         elif key in settings["move_forward"]:
    #             actor.rect.y -= speed
    #             actor.image = actor.character_image_forward
    #         elif key in settings["move_backward"]:
    #             actor.rect.y += speed
    #             actor.image = actor.character_image_backward

    #     actors.clear(scr, bg)
    #     npcs.clear(scr, bg)
    #     actors.draw(scr)
    #     npcs.draw(scr)

    #     pygame.display.update()
    #     pygame.display.flip()
