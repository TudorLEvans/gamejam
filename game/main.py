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
from .sprites import platform, player



def mainGame(screen,width,height):
    running = True

    gravity =  0.5
    frame_rate = 60
    movement_speed = 0.5

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    non_player_sprites = pygame.sprite.Group()

    levels = pygame.sprite.Group()

    clock = pygame.time.Clock()

    playerSprite = player.Player(levels,width,height,gravity,movement_speed, non_player_sprites)

    all_sprites.add(playerSprite)

    platform_array = [[250,550],[300,550]]

    for items in platform_array:
        platformSprite = platform.Platform(items[0],items[1])
        levels.add(platformSprite)
        all_sprites.add(platformSprite)
        non_player_sprites.add(platformSprite)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    playerSprite.accelerate(1)
                if event.key == K_DOWN:
                    playerSprite.accelerate(-1)
            if event.type == KEYUP:
                if event.key == K_UP:
                    playerSprite.accelerate(-1)
                if event.key == K_DOWN:
                    playerSprite.accelerate(1)

        screen.fill((0,0,0))
        playerSprite.update()
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()
        clock.tick(20)

    pygame.quit()