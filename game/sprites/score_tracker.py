import pygame,sys

class Score(pygame.sprite.Sprite):
    def __init__(self, journey_length):
        super(Score, self).__init__()
        
        self.surf = pygame.Surface((0, 10))
        self.surf.fill((200, 50, 200))
        self.rect = self.surf.get_rect()


    def update_score(self, screen_width, journey_length, distance):
        score = screen_width*distance/journey_length
        self.surf = pygame.Surface((score, 10))
        self.surf.fill((200, 50, 200))
        self.rect = self.surf.get_rect()