#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import pygame
import xml.etree.ElementTree as ET
from logger import get_logger
from _init_settings import *
pygame.init()
                
def get_map(map_file: str, tiles_file_ext: str = "png") -> pygame.Surface:
    root = ET.parse(f"{maps_path}\\{map_file}").getroot()
    scr = pygame.Surface((int(root.attrib["width"])*int(root.attrib["tilewidth"]), int(root.attrib["height"])*int(root.attrib["tileheight"])))
    
    tile_img = pygame.image.load(f'{tiles_path}\\{os.path.splitext(root.find("tileset").attrib["source"])[0]}.{tiles_file_ext}')
    tiles = {}
    tile_counter = int(root.find("tileset").attrib["firstgid"])
    for y in range(0, tile_img.get_height(), int(root.find("editorsettings")[0].attrib["height"])):
        for x in range(0, tile_img.get_width(), int(root.find("editorsettings")[0].attrib["width"])):
            tiles[tile_counter] = (x, y, int(root.attrib["tilewidth"]), int(root.attrib["tileheight"]))
            tile_counter += 1
            
    for layer in root.findall("layer"):
        y = 0
        for row in layer[0].text.split("\n")[1:-1]:
            x = 0
            for elem in row[:-1].split(","):
                scr.blit(tile_img, (x, y), (tiles[int(elem)]))
                x += int(root.attrib["tilewidth"])
            y += int(root.attrib["tileheight"])
            
    objects = []
    
    return scr, objects

if __name__ == "__main__":
    scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    while True:
        map0, map0_objects = get_map("test.tmx")
        scr.blit(map0, (0, 0))
        
        pygame.display.update()
        pygame.display.flip()