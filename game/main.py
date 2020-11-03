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



def mainGame():
    pygame.init()

    running = True

    size = width, height = 600, 600
    gravity =  0.5
    frame_rate = 60
    movement_speed = 5

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    levels = pygame.sprite.Group()

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    playerSprite = player.Player(levels,width,height,gravity,movement_speed)
    all_sprites.add(playerSprite)

    platform_array = [[0,200],[200,200],[250,200]]

    for items in platform_array:
        platformSprite = platform.Platform(items[0],items[1])
        levels.add(platformSprite)
        all_sprites.add(platformSprite)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    playerSprite.stop_walk(-1)
                if event.key == K_RIGHT:
                    playerSprite.stop_walk(1)

        screen.fill((0,0,0))
        pressed_keys = pygame.key.get_pressed()
        playerSprite.set_speeds(pressed_keys)
        playerSprite.update()
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()
        clock.tick(20)

    pygame.quit()