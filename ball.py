import pygame
import random
import os

assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed, paddle, group_all, group_self, group_blocks):
        super().__init__(group_self, group_all)
        self.image = pygame.image.load(os.path.join(assets_dir, "ball.png")).convert_alpha()#Название пнгшки
        self.image = pygame.transform.scale(self.image, (size, size))#Редачу размер
        self.rect = self.image.get_rect(center=(x, y))#ограничивающии прямоугольник
        self.vx = random.choice([-4, 4])
        self.vy = -speed
        self.paddle = paddle
        self.group_blocks = group_blocks
    
    def update(self, screen_width, screen_height):
        #Меняем позицию
        self.rect.x += self.vx
        self.rect.y += self.vy

        #Столкновение со стенами
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.vx = -self.vx
        if self.rect.top <= 0:
            self.vy = -self.vy

        #Улетел вниз(kill() - удаляет спрайт полность из всех групп)
        if self.rect.bottom >= screen_height:
            self.kill()

        if self.rect.colliderect(self.paddle.rect):#Проверка столновения self с ракеткой за этот тик
            self.vy = -abs(self.vy)#Вектор скорости по y на положительный
            offset = (self.rect.centerx - self.paddle.rect.centerx) / (self.paddle.rect.width // 2)#Что бы не было застревания
            self.vx += offset * 2
            self.vx = max(min(self.vx, 6), -6)#Угол отдаления
        
        for block in self.group_blocks:
            if self.rect.colliderect(block.rect):
                self.vy = -self.vy#Вектор скорости по y на положительный
                offset = (self.rect.centerx - block.rect.centerx) / (block.rect.width // 2)#Что бы не было застревания
                self.vx += offset * 2
                self.vx = max(min(self.vx, 6), -6)#Угол отдаления
                if block.block_type != 1:#1 не разрушаемые блоки
                    block.kill()