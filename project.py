import pygame
import random
import os

pygame.init()

width, height = 1080, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping-pong")#Название окна
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
balls = pygame.sprite.GroupSingle()

assets_dir = os.path.join(os.path.dirname('C:\C++\sprite'), 'sprite')#Путь до спрайтов + название папки

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, balls)
        self.image = pygame.image.load(os.path.join(assets_dir, "ball.png")).convert_alpha()#Название пнгшки
        self.image = pygame.transform.scale(self.image, (15, 15))#Редачу размер
        self.rect = self.image.get_rect(center=(x, y))#ограничивающии прямоугольник
        self.vx = random.choice([-4, 4])
        self.vy = -8
    
    def update(self):
        #Меняем позицию
        self.rect.x += self.vx
        self.rect.y += self.vy

        #Столкновение со стенами
        if self.rect.left <= 0 or self.rect.right >= width:
            self.vx = -self.vx
        if self.rect.top <= 0:
            self.vy = -self.vy

        #Улетел вниз(kill() - удаляет спрайт полность из всех групп)
        if self.rect.bottom >= height:
            self.kill()

        if self.rect.colliderect(paddle.rect):#Проверка столновения self с ракеткой за этот тик
            self.vy = -abs(self.vy)#Вектор скорости по y на положительный
            offset = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width // 2)#Что бы не было застревания
            self.vx += offset * 2
            self.vx = max(min(self.vx, 6), -6)#Угол отдаления


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)#Наследование(Хз в лекции так)
        self.image = pygame.image.load(os.path.join(assets_dir, "platform.png")).convert_alpha()#Название пнгшки
        self.image = pygame.transform.scale(self.image, (120, 15))#Редачу размер
        self.rect = self.image.get_rect(midbottom=(width // 2, height - 30))#Ограничивающии прямоугольник
        self.speed = 10

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
        if self.rect.right > width:
            self.rect.right = width


paddle = Paddle()#Ракетка
Ball(width // 2, height - 60)#Старторый мячик на ракетке


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if len(balls) == 0:#Проигрыш
        running = False#Пока что сразу выход(Добавить менюшку рестарта)

    all_sprites.update()#Обновление всех спрайтов(Позиции состояние)

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()