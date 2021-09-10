#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import pygame
import xml.etree.ElementTree as ET
from logger import get_logger
from _init_settings import *
pygame.init()

class Objects(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
                
def get_map(map_file: str, tiles_file_ext: str = "png") -> tuple:
    """
    Makes map and objects out of xml file

    Args:
        map_file (str): file with map\n
        tiles_file_ext (str, optional): extension of files containing tiles. Defaults to "png".\n

    Returns:
        tuple: tuple containing pygame.Surface with map and objects sprite
    """
    log = get_logger(__file__)
    root = ET.parse(f"{maps_path}\\{map_file}").getroot()
    scr = pygame.Surface((int(root.attrib["width"])*int(root.attrib["tilewidth"]), int(root.attrib["height"])*int(root.attrib["tileheight"])))
    
    tile_img = pygame.image.load(f'{tiles_path}\\{os.path.splitext(os.path.split(root.find("tileset").attrib["source"])[-1])[0]}.{tiles_file_ext}').convert_alpha()
    tiles = {}
    tile_counter = int(root.find("tileset").attrib["firstgid"])
    for y in range(0, tile_img.get_height(), int(root.find("editorsettings")[0].attrib["height"])):
        for x in range(0, tile_img.get_width(), int(root.find("editorsettings")[0].attrib["width"])):
            tiles[tile_counter] = (x, y, int(root.attrib["tilewidth"]), int(root.attrib["tileheight"]))
            tile_counter += 1
    log.debug("Tileset dict done")
            
    layers = {}
    for layer in root.findall("layer"):
        properties = {}
        for property in layer.find("properties"):
            properties[property.attrib["name"]] = property.attrib["value"]
        layers[layer.find("data").text.strip()] = properties
    log.debug("Layers dict done")
    
    unsorted_dict = {}
    for data, properties in layers.items():
        unsorted_dict[properties["z-index"]] = data
    sorted_dict = dict(sorted(unsorted_dict.items()))
    for data in sorted_dict.values():
        properties = layers[data]
        layers.pop(data)
        layers[data] = properties
    log.debug("Layers dict sorted")
            
    for layer in layers:
        y = 0
        for row in layer.split("\n"):
            x = 0
            for elem in row.strip("\n\t, ").split(","):
                if elem != "0":
                    scr.blit(tile_img, (x, y), (tiles[int(elem)]))
                x += int(root.attrib["tilewidth"])
            y += int(root.attrib["tileheight"])
    log.debug("Map surface done")
            
    objects_scr = pygame.Surface((int(root.attrib["width"])*int(root.attrib["tilewidth"]), int(root.attrib["height"])*int(root.attrib["tileheight"])))
    for object_group in root.findall("objectgroup"):
        for object in object_group.findall("object"):
            try:
                if object[0].tag == "polygon":
                    points = []
                    for point in object[0].attrib["points"].split(" "):
                        points.append((float(object.attrib["x"])+float(point.split(",")[0]), float(object.attrib["y"])+float(point.split(",")[1])))
                    pygame.draw.polygon(objects_scr, (255, 165, 0), points, width = 0)
                elif object[0].tag == "ellipse":
                    pygame.draw.ellipse(objects_scr, (255, 165, 0), (float(object.attrib["x"]), float(object.attrib["y"]), float(object.attrib["width"]), float(object.attrib["height"])), width = 0)
                elif object[0].tag == "point":
                    pygame.draw.rect(objects_scr, (255, 165, 0), (float(object.attrib["x"]), float(object.attrib["y"]), 1, 1), width = 0)
            except IndexError: #Fucking rectangle
                pygame.draw.rect(objects_scr, (255, 165, 0), (float(object.attrib["x"]), float(object.attrib["y"]), float(object.attrib["width"]), float(object.attrib["height"])), width = 0)
    objects_sprite = Objects()
    objects_sprite.mask = pygame.mask.from_surface(objects_scr)
    log.debug("Objects sprite done")
        
    log.info(f"Map {map_file} done succesfully")
    return scr.convert_alpha(), objects_sprite

if __name__ == "__main__":
    scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    map0, map0_sprite = get_map("test.tmx")
    #print(pygame.sprite.collide_mask(map0_sprite, char_group.sprite, False))

    while True:
        scr.blit(map0, (0, 0))
        
        pygame.display.update()
        pygame.display.flip()