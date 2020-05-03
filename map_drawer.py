#!/usr/bin/python3
#-*- coding: utf-8 -*-

import xml_parser
import pygame

def map_drawer(scr, path_to_map, x = 0, y = 0, path_to_squares = "images/squares.png", count_of_lines = 16, count_of_column = 30, size_of_plate = 16):
    y_position = y

    list_of_squares = []
    map = []

    parsed_xml = xml_parser.parse(path_to_map)
    squares = pygame.image.load(path_to_squares)

    # Создаем список с координатами квадратов для карты
    for y_position_of_square in range(0, count_of_lines * size_of_plate, size_of_plate):
        for x_position_of_square in range(0, count_of_column * size_of_plate, size_of_plate):
            list_of_squares.append((x_position_of_square, y_position_of_square))

    # Создаем список с номерами квадратов из карты
    for i in range(len(parsed_xml)):
        splitted_line = (parsed_xml[i].split(","))
        if i < len(parsed_xml) - 1:
            del splitted_line[len(splitted_line) - 1]
        map.append(splitted_line)

    scr.fill((0, 0, 0))

    # Рисуем карту по списку с номерами квадратов карты
    for line in map:
        x_position = x
        for plate_num in line:
            try:
                plate = list_of_squares[int(plate_num) - 5]
                scr.blit(squares, (x_position, y_position), (plate[0], plate[1], size_of_plate, size_of_plate))
            except Exception:
                no_plate = pygame.image.load("images/no_plate.png")
                scr.blit(no_plate, (x_position, y_position))
            x_position += size_of_plate
        y_position += size_of_plate