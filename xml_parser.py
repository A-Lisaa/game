#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lxml import etree

def parse(xml_file):
    """
    Парсинг XML-файлов, в качестве аргумента - путь до файла
    """
    with open(xml_file) as f:
        xml = f.read()
    
    root = etree.fromstring(xml)

    map = []
    
    for appt in root.getchildren():
        for elem in appt.getchildren():
            text = elem.text
            map = text.split("\n")
            del map[0]
            del map[len(map) - 1]

    return map