import pygame
import os
from paddle import Paddle
from ball import Ball
from block import Block
from level_loader import load_level
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

paddle_speed = int(config['PADDLE']['speed'])
paddle_width, paddle_height = int(config['PADDLE']['width']), int(config['PADDLE']['height'])
paddle_indent = int(config['PADDLE']['indent'])

block_size = int(config['BLOCK']['size'])

ball_size = int(config['BALL']['size'])
ball_speed = int(config['BALL']['speed'])
ball_indent = int(config['BALL']['indent'])

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

paddle = Paddle(width, height, paddle_width, paddle_height, paddle_speed, paddle_indent, all_sprites)#Ракетка
Ball(width // 2, height - ball_indent, ball_size, ball_speed, paddle, all_sprites, balls, blocks)#Старторый мячик на ракетке

load_level(1, block_size, width, height, all_sprites, blocks)#Уровни некоректно отображаются

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if len(balls) == 0:#Проигрыш
        running = False#Пока что сразу выход(Добавить менюшку рестарта)

    paddle.update()
    balls.update(width, height)
    
    screen.fill((30, 30, 45))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()