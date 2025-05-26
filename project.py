import pygame
import os
from paddle import Paddle
from ball import Ball
from block import Block
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

pygame.init()

size = pygame.display.get_desktop_sizes()#что бы на всех компьютерах работало корректно
width = size[0][0]
height = size[0][1]

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping-pong")#Название окна
pygame.display.toggle_fullscreen()#Полноэкранный режим
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
blocks = pygame.sprite.Group()

paddle = Paddle(width, height, all_sprites)#Ракетка
Ball(width // 2, height - 60, paddle, all_sprites, balls, blocks)#Старторый мячик на ракетке

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