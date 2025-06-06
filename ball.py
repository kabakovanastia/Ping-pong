import pygame
import random
import math
import os
from random import randint
from boosts import Boost

assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
pygame.mixer.init()
sound_break = pygame.mixer.Sound("assets/special_sound/breaking.mp3")
sound_drop_bonus = pygame.mixer.Sound("assets/special_sound/drop_bonus.mp3")
sound_break.set_volume(0.5)
sound_drop_bonus.set_volume(0.7)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed, paddle, group_all, group_self, group_blocks, group_boosts):
        super().__init__(group_self, group_all)
        self.image = pygame.image.load(os.path.join(assets_dir, "ball.png")).convert_alpha()#Название пнгшки
        self.image = pygame.transform.scale(self.image, (size, size))#Редачу размер
        self.rect = self.image.get_rect(center=(x, y))#ограничивающии прямоугольник
        self.vx = 0
        self.vy = -speed
        self.paddle = paddle
        self.group_self = group_self
        self.group_blocks = group_blocks
        self.group_all = group_all
        self.group_boosts = group_boosts

    
    def update(self, screen_width, screen_height):
        #Меняем позицию
        self.rect.x += self.vx
        self.rect.y += self.vy

        #Столкновение со стенами
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.vx = -self.vx
            self.rect.x += self.vx
        if self.rect.top <= 0:
            self.vy = -self.vy
            self.rect.y += self.vy
            self.rect.top += 15

        #Улетел вниз(kill() - удаляет спрайт полность из всех групп)
        if self.rect.bottom >= screen_height:
            self.kill()

        if self.rect.colliderect(self.paddle.rect) and self.vy > 0:
                # Центр мяча и ракетки
                ball_center = self.rect.centerx
                paddle_center = self.paddle.rect.centerx
                distance = ball_center - paddle_center

                # Относительная позиция от центра (-1 до 1)
                offset = distance / (self.paddle.rect.width / 2)

                # Максимальный угол отражения
                max_angle = math.radians(60)

                # Угол отскока
                angle = offset * max_angle

                speed = math.hypot(self.vx, self.vy)  # сохранить общую скорость
                self.vx = speed * math.sin(angle)
                self.vy = -self.vy
        
        for block in self.group_blocks:
            if self.rect.colliderect(block.rect):
                self.vy = -self.vy#Вектор скорости по y на положительный
                offset = (self.rect.centerx - block.rect.centerx) / (block.rect.width // 2)#Что бы не было застревания
                self.vx += offset * 2
                self.vx = max(min(self.vx, 6), -6)#Угол отдаления
                self.rect.centerx += self.vx
                self.rect.centery += self.vy
                if block.block_type != 1:#1 не разрушаемые блоки
                    block.kill()
                    sound_break.play()
                    if random.randint(1, 8) == 1:
                        if random.randint(1, len(self.group_self)) == 1:
                            Boost("*", block.rect.x, block.rect.y, self.group_all, self.group_boosts)
                            sound_drop_bonus.play()
                        else:
                            Boost("+", block.rect.x, block.rect.y, self.group_all, self.group_boosts)
                            sound_drop_bonus.play()