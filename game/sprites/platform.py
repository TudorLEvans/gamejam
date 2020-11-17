import pygame,sys
import pymunk

class Platform(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, radius, mass_ratio, is_moon, image):
        super(Platform, self).__init__()
        
        self.surf = image
        self.surf = pygame.transform.scale(self.surf, (600, 600))


        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = position_x, position_y
        self.shape = pymunk.Segment(self.body, (0, 0), (600, 0), radius)

        self.is_moon = is_moon
        self.radius = radius
        self.mass_ratio = mass_ratio

    def get_center(self):
        return self.radius + self.rect.centery - 500/2

    @property
    def topleft(self):
        return self.body.position
