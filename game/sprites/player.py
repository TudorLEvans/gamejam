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

class Player(pygame.sprite.Sprite):
    def __init__(self,levels,width,height,gravity,movement_speed):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 40))
        self.surf.fill((50, 50, 255))
        self.rect = self.surf.get_rect()
        self.rect.bottom = 550
        self.rect.left = 290
        self.v_y = 0
        self.v_x = 0
        self.levels = levels
        self.width = width
        self.height = height
        self.gravity = gravity
        self.movement_speed = movement_speed
        self.thrust = 0

    def update(self):
        self.calculate_gravity()
        self.v_y += self.thrust*self.movement_speed
        if self.rect.bottom > self.height:
            self.rect.bottom = self.height 
            self.v_y = 0
        self.rect.move_ip(self.v_x,self.v_y)
        self.level_collision_detector()

    
    def calculate_gravity(self):
        self.rect.y += 2
        is_on_platform = pygame.sprite.spritecollideany(self,self.levels)
        self.rect.y -= 2
        if is_on_platform == None:
            self.v_y += 500/(1000+self.height-self.rect.centery)

    def accelerate(self,direction):
        if (self.thrust >-1 and direction == 1) or (self.thrust <1 and direction == -1):
            self.thrust -= direction
    
    def level_collision_detector(self):
        collision_point = pygame.sprite.spritecollideany(self,self.levels)
        if collision_point != None:
            if self.v_x > 0 and collision_point.rect.left >= self.rect.right - self.v_x:
                self.rect.right = collision_point.rect.left
                self.v_x = 0
            if self.v_x < 0 and collision_point.rect.right <= self.rect.left - self.v_x:              
                self.rect.left = collision_point.rect.right
                self.v_x = 0
            if self.v_y < 0 and collision_point.rect.bottom <= self.rect.top - self.v_y:
                self.rect.top = collision_point.rect.bottom
                self.v_y = 0
            if self.v_y > 0 and collision_point.rect.top >= self.rect.bottom - self.v_y:
                self.rect.bottom = collision_point.rect.top
                self.v_y = 0
                self.v_x = 0
                