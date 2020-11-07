import pygame,sys

class Background(pygame.sprite.Sprite):
    def __init__(self, position_x,position_y):
        super(Background, self).__init__()
        self.surf = pygame.image.load("images/background.png")
        self.rect = self.surf.get_rect()
        self.rect.topleft = position_x,position_y