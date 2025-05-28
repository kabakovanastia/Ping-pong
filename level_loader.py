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
                pos_x = x * (block_size + (block_size // 4)) * 2 #размер блока меняется в зависимости от размера экрана (1 к 30) ((вроде))
                pos_y = y * (block_size + (block_size // 4)) * 2 #хуй знает почему это разделить на 4 и умножить на 2 правильно работает но всё ровно стоит
                size = width // block_size
                Block(pos_x, pos_y, size, block_type, group_all, group_self)