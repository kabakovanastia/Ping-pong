import pygame
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

boost_size = int(config["BOOST"]["size"])
boost_speed = int(config["BOOST"]["speed"])

assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

class Boost(pygame.sprite.Sprite):
    def __init__(self, boost_type, x, y, group_all, group_self):
        super().__init__(group_all, group_self)
        if boost_type == "+":
            self.image = pygame.image.load(os.path.join(assets_dir, "bonus_add_three_ball.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(assets_dir, "bonus_triple_ball.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (boost_size, boost_size))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -boost_speed
        self.boost_type = boost_type
    
    def update(self):
        self.rect.y -= self.speed