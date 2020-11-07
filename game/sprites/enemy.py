import pygame,sys
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Enemy, self).__init__()

        self.width, self.height = 25, 40
        self.screen_width, self.screen_height = screen_width, screen_height
        self.thrust_magnitude, self.thrust_direction = 1, 1

        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((52, 255, 41))
        self.rect = self.surf.get_rect()
        self.rect.center = (screen_width, 0)

    def update(self):
        # Check if need to change direction
        if self.rect.right >= self.screen_width or self.rect.left <= 0:
                self.thrust_direction *= -1

        self.rect.move_ip(self.thrust_direction * self.thrust_magnitude, 0)
            