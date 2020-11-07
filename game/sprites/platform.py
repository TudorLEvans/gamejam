import pygame,sys

class Platform(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, radius, mass_ratio, is_moon):
        super(Platform, self).__init__()
        
        self.surf = pygame.Surface((600, 600))
        self.surf.fill((200, 50, 50))
        self.rect = self.surf.get_rect()
        self.rect.topleft = position_x, position_y

        self.is_moon = is_moon
        self.radius = radius
        self.mass_ratio = mass_ratio

    def get_center(self):
        return self.radius + self.rect.centery - 500/2