import pygame
import os


class Music:
    def __init__(self, volume, music_folder = "assets/music/"):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.music_list = []
        self.current_song = 0
        self.volume = volume
        self.add_music(self.music_folder)

    def add_music (self, music_folder):
        for file in os.listdir(music_folder):
            if file: self.music_list.append(os.path.join(music_folder, file))

    def play(self):
        pygame.mixer.music.load(self.music_list[self.current_song])
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()
    
    def check_song(self):
        if not pygame.mixer.music.get_busy():
            self.current_song = (self.current_song + 1) % len(self.music_list)
            self.play()