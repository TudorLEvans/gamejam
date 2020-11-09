import pygame,sys

class Timer(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Timer, self).__init__()
        
        self.font = pygame.font.Font(None, 20)
        self.surf = self.font.render("{} s".format(0), True, [255, 255, 255], None)
        self.rect = (screen_width - 30, screen_height - 30)

    def update_time(self, screen_width, screen_height, time):
        time_in_s = time/1000
        self.surf = self.font.render("{} s".format(int(time_in_s)), True, [255, 255, 255], None)
        self.rect = (screen_width - 60, screen_height - 30)