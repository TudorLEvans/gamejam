import pygame,sys

class Speedometer(pygame.sprite.Sprite):
    def __init__(self, screen_height):
        super(Speedometer, self).__init__()
        
        self.font = pygame.font.Font(None, 20)
        self.surf = self.font.render("{} mps".format(0), True, [255, 255, 255], None)
        self.rect = (30, screen_height - 30)

    def update_speed(self, screen_height, v_x):
        self.surf = self.font.render("{} mps".format(-int(v_x)), True, [255, 255, 255], None)
        self.rect = (30, screen_height - 30)