import pygame,sys

class Speedometer(pygame.sprite.Sprite):
    def __init__(self, screen_height):
        super(Speedometer, self).__init__()
        
        self.font = pygame.font.Font(None, 20)
        self.surf = self.font.render("vel = {} mps, acc = {}mps2".format(0,0), True, [255, 255, 255], None)
        self.rect = (30, screen_height - 30)

    def update_speed(self, screen_height, v_y, a_y):
        self.surf = self.font.render("vel = {} mps, acc = {}mps2".format(round(-int(v_y),2), round(-a_y,2)), True, [255, 255, 255], None)
        self.rect = (30, screen_height - 30)