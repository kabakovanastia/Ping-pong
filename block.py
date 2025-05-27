import pygame
import os

assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, size, block_type, group_all, group_self):#Блок тайп: 0 - нету, 1 - неразруш, 2-5 - цвета
        super().__init__(group_all, group_self)
        self.block_type = block_type
        self.image = pygame.image.load(os.path.join(assets_dir, f'brick_{block_type}.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))