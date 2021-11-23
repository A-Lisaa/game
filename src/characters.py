import __init__
import pygame
from character_class import Character
pygame.init()

chars = pygame.sprite.Group()

sammy = Character("Samantha", "samantha", (400, 300))
chars.add(sammy)
npc0 = Character("Npc0", "samantha", (200, 100))
chars.add(npc0)