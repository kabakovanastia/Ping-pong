import pygame
import os

assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, block_type, group_all, group_self):#Блок тайп это разрушаемые неразрушаем розовые красные и тд ассета
        super().__init__(group_all, group_self)
        self.brick_type = block_type
        self.image = pygame.image.load(os.path.join(assets_dir, f'brick{block_type}.png')).convert_alpha()#Надо переименовать ассеты что бы эта часть кода корекктно работала вместо block_type будет рисоваться блок
        self.image = pygame.transform.scale(self.image, (width // 50, width // 50))
        self.rect = self.image.get_rect(center=(x, y))