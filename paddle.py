import pygame
import os

assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

class Paddle(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, group_all):
        super().__init__(group_all)#Наследование(Хз в лекции так)
        self.image = pygame.image.load(os.path.join(assets_dir, "platform.png")).convert_alpha()#Название пнгшки
        self.image = pygame.transform.scale(self.image, (160, 15))#Редачу размер
        self.rect = self.image.get_rect(midbottom=(screen_width // 2, screen_height - 30))#Ограничивающии прямоугольник
        self.speed = 10
        self.screen_width = screen_width

    #Управление на стрелочки
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        #Уперся в стену
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width