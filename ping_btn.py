import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
DARKEN = (0, 0, 0, 180)

# Состояния
paused = False
in_main_menu = True

#кнопки
def draw_button(text, rect, mouse_pos, active_color, inactive_color):
    color = active_color if rect.collidepoint(mouse_pos) else inactive_color
    pygame.draw.rect(screen, color, rect)
    txt = font.render(text, True, WHITE)
    txt_rect = txt.get_rect(center=rect.center)
    screen.blit(txt, txt_rect)

#главное меню
def show_main_menu():
    screen.fill(BLUE)
    mouse_pos = pygame.mouse.get_pos()
    
    start_btn = pygame.Rect(300, 220, 200, 50)
    exit_btn = pygame.Rect(300, 300, 200, 50)

    draw_button("Старт", start_btn, mouse_pos, (0, 200, 0), (0, 100, 0))
    draw_button("Выход", exit_btn, mouse_pos, (200, 0, 0), (100, 0, 0))

    return start_btn, exit_btn

#меню паузы
def show_pause_menu():
    dark_overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    dark_overlay.fill(DARKEN)
    screen.blit(dark_overlay, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    continue_btn = pygame.Rect(300, 220, 200, 50)
    exit_btn = pygame.Rect(300, 300, 200, 50)

    draw_button("Продолжить", continue_btn, mouse_pos, (0, 200, 0), (0, 100, 0))
    draw_button("Выход", exit_btn, mouse_pos, (200, 0, 0), (100, 0, 0))

    return continue_btn, exit_btn

#меню рестарт 
def show_restart_menu():
    dark_overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    dark_overlay.fill(DARKEN)
    screen.blit(dark_overlay, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    restart_btn = pygame.Rect(300, 220, 200, 50)
    exit_btn = pygame.Rect(300, 300, 200, 50)

    draw_button("Продолжить", restart_btn, mouse_pos, (0, 200, 0), (0, 100, 0))
    draw_button("Выход", exit_btn, mouse_pos, (200, 0, 0), (100, 0, 0))

    return restart_btn, exit_btn 

#меню между уровнями
def show_next_level_menu():
    dark_overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    dark_overlay.fill(DARKEN)
    screen.blit(dark_overlay, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    next_Level_btn = pygame.Rect(300, 220, 200, 50)
    exit_btn = pygame.Rect(300, 300, 200, 50)

    draw_button("Следующий уровень", next_Level_btn, mouse_pos, (0, 200, 0), (0, 100, 0))
    draw_button("Выход", exit_btn, mouse_pos, (200, 0, 0), (100, 0, 0))

    return next_Level_btn, exit_btn