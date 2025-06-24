import pygame
import os
import sys

class AnimatedBanana:
    def __init__(self, x, y, scale=0.5):  # По умолчанию уменьшен в 2 раза (0.5)
        self.x = x
        self.y = y
        self.scale = scale
        self.animation_speed = 0.1
        self.current_frame = 0
        self.animation_frames = []
        self.load_animation_frames()
        self.image = self.animation_frames[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.is_animating = True
        
    def load_animation_frames(self):
        try:
            # Загрузка спрайт-листа
            sprite_sheet = pygame.image.load(os.path.join("assets", "Dance.png")).convert_alpha()
            
            # Размеры оригинального спрайта
            original_width = sprite_sheet.get_width() // 4  # 4 кадра в ширину
            original_height = sprite_sheet.get_height()
            
            # Новые размеры с учётом масштаба
            new_width = int(original_width * self.scale)
            new_height = int(original_height * self.scale)
            
            # Вырезаем и масштабируем каждый кадр
            for i in range(4):
                frame = sprite_sheet.subsurface((i * original_width, 0, original_width, original_height))
                frame = pygame.transform.scale(frame, (new_width, new_height))
                self.animation_frames.append(frame)
                
        except Exception as e:
            print(f"Ошибка загрузки спрайтов: {e}")
            # Создаём заглушку
            frame = pygame.Surface((32, 32), pygame.SRCALPHA)
            pygame.draw.circle(frame, (255, 255, 0), (16, 16), 16)
            self.animation_frames = [frame] * 4
    
    # Остальные методы без изменений
    def update(self):
        if self.is_animating:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.animation_frames):
                self.current_frame = 0
            self.image = self.animation_frames[int(self.current_frame)]
            self.rect = self.image.get_rect(center=(self.x, self.y))
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))


# Пример использования с маленьким бананом
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # Создаём банан в 2 раза меньше оригинального размера (scale=0.5)
    banana = AnimatedBanana(400, 300, scale=0.5)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        banana.update()
        
        screen.fill((50, 50, 50))
        banana.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()