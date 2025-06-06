import pygame
import os
from paddle import Paddle
from ball import Ball
from heart import Heart
from button import Button
from block import Block
from heart import create_hearts
from level_loader import load_level, count_unbreak
from music import Music
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

current_level = int(config['LEVEL']['current'])

heart_count = int(config["HEART"]["count"])

button_height = int(config['BUTTON']['height'])

pygame.init()

size = pygame.display.get_desktop_sizes()
width = size[0][0]
height = size[0][1]

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping-pong")
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
blocks = pygame.sprite.Group()
boosts = pygame.sprite.Group()
hearts = pygame.sprite.Group()
buttons = pygame.sprite.Group()

muzlo = Music(0.02)
muzlo.play()
sound_get_bonus = pygame.mixer.Sound("assets/special_sound/get_bonus.mp3")
sound_get_bonus.set_volume(0.5)

but_play = Button(width // 2, height // 2, 'play', width, height, buttons)
but_exit = Button(width // 2, height // 2 + (height // button_height) * 1.5, 'exit', width, height, buttons)

def start_game(load=True):
    if load:
        load_level(current_level, block_size, width, height, all_sprites, blocks)
    Ball(width // 2, height - ball_indent, ball_size, ball_speed, paddle, all_sprites, balls, blocks, boosts)
    create_hearts(heart_count, all_sprites, hearts)

paddle = Paddle(width, height, paddle_width, paddle_height, paddle_speed, paddle_indent, all_sprites)
start_game()

is_paused = True
running = True
while running:
    muzlo.check_song()
    unbreak = count_unbreak(current_level)

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            is_paused = not is_paused
        if is_paused:
            if event.type == pygame.MOUSEBUTTONDOWN and but_play.rect.collidepoint(pygame.mouse.get_pos()):
                is_paused = not is_paused
            if event.type == pygame.MOUSEBUTTONDOWN and but_exit.rect.collidepoint(pygame.mouse.get_pos()):
                running = False

    if not is_paused:
        if len(boosts) != 0:
            for sprite in boosts:
                if sprite.rect.colliderect(paddle.rect):
                    if sprite.boost_type == "+":
                        Ball(paddle_width // 2 + paddle.rect.x - ball_indent // 2, height - ball_indent, ball_size, ball_speed, paddle, all_sprites, balls, blocks, boosts)
                        Ball(paddle_width // 2 + paddle.rect.x, height - ball_indent, ball_size, ball_speed, paddle, all_sprites, balls, blocks, boosts)
                        Ball(paddle_width // 2 + paddle.rect.x + ball_indent // 2, height - ball_indent, ball_size, ball_speed, paddle, all_sprites, balls, blocks, boosts)
                        sound_get_bonus.play()
                    else:
                        for ball in balls:
                            for i in range(2):
                                Ball(ball.rect.x, ball.rect.y, ball_size, ball_speed, paddle, all_sprites, balls, blocks, boosts)
                                sound_get_bonus.play()
                    sprite.kill()

        if (len(blocks) - unbreak) == 0:

            current_level += 1
            if current_level == 6:
                current_level = 1

            for sprite in all_sprites:
                if not isinstance(sprite, Heart):
                    sprite.kill()
            paddle = Paddle(width, height, paddle_width, paddle_height, paddle_speed, paddle_indent, all_sprites)
            start_game()
            is_paused = True
            
        if len(balls) == 0:
            heart_count -= 1
            if heart_count == 0:
                current_level = 1
                heart_count = 3
                for sprite in all_sprites:
                    if isinstance(sprite, Block):
                        sprite.kill()
                paddle.kill()
                paddle = Paddle(width, height, paddle_width, paddle_height, paddle_speed, paddle_indent, all_sprites)
                start_game()
                is_paused = True
            else:
                for heart in hearts:
                    heart.kill()
                paddle.kill()
                paddle = Paddle(width, height, paddle_width, paddle_height, paddle_speed, paddle_indent, all_sprites)
                start_game(False)
                is_paused = True
    
        paddle.update()
        balls.update(width, height)
        boosts.update()

    screen.fill((30, 30, 45))
    all_sprites.draw(screen)

    if is_paused:
        overlay = pygame.Surface((width, height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        buttons.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

