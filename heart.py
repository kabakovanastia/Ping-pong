import pygame
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

heart_size = int(config["HEART"]["size"])
heart_indent = int(config["HEART"]["indent"])

assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y, group_all, group_self):
        super().__init__(group_all, group_self)
        self.image = pygame.image.load(os.path.join(assets_dir, "heart.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (heart_size, heart_size))
        self.rect = self.image.get_rect(center=(x, y))

def create_hearts(heart_count, group_all, group_self):
    for i in range(heart_count):
        Heart(heart_indent + i * heart_size, heart_indent, group_all, group_self)