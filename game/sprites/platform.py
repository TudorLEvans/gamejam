import pygame,sys

class Platform(pygame.sprite.Sprite):
    def __init__(self, position_x,position_y):
        super(Platform, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((200, 50, 50))
        self.rect = self.surf.get_rect()
        self.rect.topleft = position_x,position_y