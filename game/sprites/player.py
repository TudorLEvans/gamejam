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
    def __init__(self, screen_width, screen_height, player_image):
        super(Player, self).__init__()

        self.width = 25
        self.height = 40

        self.original_surf = player_image
        self.original_surf = pygame.transform.scale(player_image, (50,120))
        # self.original_surf.fill((50, 255, 50))

        self.surf = self.original_surf
        self.rect = self.surf.get_rect(center = (screen_width//2, screen_height//2))

        self.start_height = self.rect.centery

        self.v_x = 0
        self.v_y = 0
        
        self.a_x = 0
        self.a_y = 0
        
        self.thrust_magnitude = 0.4
        self.thrust_direction = 0

        self.rotational_speed = 1
        self.angle = 0
        self.cos_angle = 1
        self.sin_angle = 0


    def update(self, screen_width, gravity_constant, levels, non_player_sprites):

        self.a_x = self.thrust_direction * self.thrust_magnitude * self.sin_angle
        self.a_y = self.thrust_direction * self.thrust_magnitude * self.cos_angle

        self.calculate_gravity(gravity_constant, levels)
        self.calculate_air_resistance()

        self.v_x += self.a_x
        self.v_y += self.a_y
        
        self.rect.move_ip(-self.v_x,0)
        for sprite in non_player_sprites:
            sprite.rect.move_ip(0, -self.v_y)
    
        self.keep_in_screen(screen_width)
        win = self.planet_collision_detection(levels, non_player_sprites)
        return win
        # self.level_collision_detector(levels, non_player_sprites)

    def calculate_gravity(self, gravity_constant, levels):
        self.rect.y += 2
        is_on_platform = pygame.sprite.spritecollideany(self, levels)
        self.rect.y -= 2

        if is_on_platform == None:
            for sprite in levels:
                self.a_y += sprite.mass_ratio*gravity_constant/((sprite.get_center() - self.rect.centery))
        
    def calculate_air_resistance(self):

        # Calculate air resistance coefficient
        air_resistance_coef = 0.0002*np.exp(-(self.rect.centery - self.start_height))

        # Air resistance always acts in opposite direction to velocity
        self.air_y = -np.sign(self.v_y)*air_resistance_coef * self.v_y**2
        self.a_y += self.air_y

    def accelerate(self, direction):
        if (self.thrust_direction >-1 and direction == 1) or (self.thrust_direction <1 and direction == -1):
            self.thrust_direction -= direction

    def rotate(self,rotational_direction):
        dtheta = rotational_direction*self.rotational_speed
        self.angle += dtheta
        self.cos_angle = np.cos(self.angle * np.pi/180)
        self.sin_angle = np.sin(self.angle * np.pi/180)
        old_center = self.rect.center
        self.surf = pygame.transform.rotozoom(self.original_surf, -self.angle, 1)
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center = old_center)
    
    def level_collision_detector(self, levels, non_player_sprites):
        collision_point = pygame.sprite.spritecollideany(self, levels)
        if collision_point != None and collision_point.is_moon == False:
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
        
    def planet_collision_detection(self, levels, non_player_sprites):
        original_speed = self.v_y
        for planet in levels:
            if self.rect.bottom - 2 <= planet.rect.top and self.rect.bottom + self.v_y >= planet.rect.top and self.v_y != 0:
                self.v_y = planet.rect.top - self.rect.bottom
                for sprite in non_player_sprites:
                    sprite.rect.move_ip(0, -self.v_y)
                if abs(self.angle%360) > 10 or abs(original_speed) > 30:
                    return False
                self.v_y = 0
                self.v_x = 0
            if self.rect.top + 2 >= planet.rect.bottom and self.rect.top + self.v_y <= planet.rect.bottom  and self.v_y != 0:
                self.v_y = planet.rect.bottom - self.rect.top
                for sprite in non_player_sprites:
                    sprite.rect.move_ip(0, -self.v_y)
                self.v_y = 0
                self.v_x = 0
                if (abs(self.angle%360) > 190 or abs(self.angle%360) < 170) or abs(original_speed) > 30:
                    return False
                elif planet.is_moon:
                    return True
        return None

    def keep_in_screen(self, screen_width):
        if self.rect.left <= 0 and self.v_x >=0:
            self.rect.left = 0
            self.v_x = 0
        if self.rect.right >= screen_width and self.v_x <= 0:
            self.rect.right = screen_width
            self.v_x = 0
