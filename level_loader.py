import os
import json
from block import Block

def load_level(level_number, block_size, width, height, group_all, group_self):

    levels_path = os.path.join(os.path.dirname(__file__), 'levels.json')
    
    with open(levels_path, 'r') as f:
        data = json.load(f)

    level_data = None
    for level in data["levels"]:
        if level['level'] == level_number:
            level_data = level
            break

    layout = level_data["layout"]

    for y in range(len(layout)):
            for x in range(len(layout[y])):
                block_type = layout[y][x]
                if block_type == 0:
                    continue  # пропустить пустые блоки
                size = width // block_size
                pos_x = x * (size + size // 6)
                pos_y = y * (size + size // 6)
                Block(pos_x, pos_y, size, block_type, group_all, group_self)


def count_unbreak(level_number):
    levels_path = os.path.join(os.path.dirname(__file__), 'levels.json')
    
    with open(levels_path, 'r') as f:
        data = json.load(f)

    level_data = None
    for level in data["levels"]:
        if level['level'] == level_number:
            level_data = level
            break

    layout = level_data["layout"]
    unbreak = 0

    for y in range(len(layout)):
            for x in range(len(layout[y])):
                block_type = layout[y][x]
                if block_type == 1:
                     unbreak += 1
    
    return unbreak