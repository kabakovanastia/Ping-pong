import pygame
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

button_width = int(config['BUTTON']['width'])
button_height = int(config['BUTTON']['height'])


assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, type, screen_width, screen_height, group_self):
        super().__init__(group_self)
        self.pos_x = x
        self.pos_y = y
        self.image = pygame.image.load(os.path.join(assets_dir, f'button_{type}.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width // button_width, screen_height // button_height))
        self.rect = self.image.get_rect(midbottom=(x, y))