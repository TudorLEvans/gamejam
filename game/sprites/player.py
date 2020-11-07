import pygame,sys
import numpy as np

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

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()

        self.width = 25
        self.height = 40
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((50, 50, 255))
        self.rect = self.surf.get_rect()
        self.rect.center = (screen_width//2, screen_height//2)

        self.v_y = 0
        self.v_x = 0
        self.thrust_magnitude = 0.4
        self.thrust_direction = 0

        self.rotational_speed = 1
        self.angle = 0
        self.cos_angle = 1
        self.sin_angle = 0


    def update(self, gravity_constant, levels, non_player_sprites):
        self.calculate_gravity(gravity_constant, levels)
        self.v_x += self.thrust_direction * self.thrust_magnitude * self.sin_angle
        self.v_y += self.thrust_direction * self.thrust_magnitude * self.cos_angle
        for sprite in non_player_sprites:
            sprite.rect.move_ip(self.v_x, -self.v_y)
        self.level_collision_detector(levels, non_player_sprites)

    def calculate_gravity(self, gravity_constant, levels):
        self.rect.y += 2
        is_on_platform = pygame.sprite.spritecollideany(self, levels)
        self.rect.y -= 2
        if is_on_platform == None:
            for sprite in levels:
                self.v_y += sprite.mass_ratio*gravity_constant/((sprite.get_center() - self.rect.centery))

    def accelerate(self, direction):
        if (self.thrust_direction >-1 and direction == 1) or (self.thrust_direction <1 and direction == -1):
            self.thrust_direction -= direction

    def rotate(self,rotational_direction):
        dtheta = rotational_direction*self.rotational_speed
        self.angle += dtheta
        self.cos_angle = np.cos(self.angle * np.pi/180)
        self.sin_angle = np.sin(self.angle * np.pi/180)
        old_center = self.rect.center
        self.surf = pygame.transform.rotozoom(self.surf, -self.angle, 1)
        self.rect = self.surf.get_rect(center = old_center)

    def level_collision_detector(self, levels, non_player_sprites):
        collision_point = pygame.sprite.spritecollideany(self, levels)
        if collision_point != None:
            if self.v_x > 0 and collision_point.rect.left >= self.rect.right - self.v_x:
                self.rect.right = collision_point.rect.left
                self.v_x = 0
            if self.v_x < 0 and collision_point.rect.right <= self.rect.left - self.v_x:              
                self.rect.left = collision_point.rect.right
                self.v_x = 0
            if self.v_y < 0 and collision_point.rect.bottom <= self.rect.top - self.v_y:
                self.v_y = collision_point.rect.bottom - self.rect.top
                for sprite in non_player_sprites:
                    sprite.rect.move_ip(self.v_x, -self.v_y)
                self.v_y = 0
            if self.v_y > 0 and collision_point.rect.top >= self.rect.bottom - self.v_y:
                self.v_y = collision_point.rect.top - self.rect.bottom
                for sprite in non_player_sprites:
                    sprite.rect.move_ip(self.v_x, -self.v_y)
                self.v_y = 0
            