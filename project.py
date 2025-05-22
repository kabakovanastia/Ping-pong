import pygame
import os
from paddle import Paddle
from ball import Ball
import configparser


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

width = int(config['WINDOW']['width'])
height = int(config['WINDOW']['height'])

width = 1080
height = 640

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping-pong")#Название окна
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
balls = pygame.sprite.GroupSingle()

paddle = Paddle(width, height, all_sprites)#Ракетка
Ball(width // 2, height - 60, paddle, all_sprites, balls)#Старторый мячик на ракетке

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if len(balls) == 0:#Проигрыш
        running = False#Пока что сразу выход(Добавить менюшку рестарта)

    paddle.update()
    balls.update(width, height)
    
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()