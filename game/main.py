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
from .sprites import platform, player, background
from menu.pause import create_pause_menu
from .sprites import platform, player, background



def mainGame(screen, screen_width, screen_height):
    running = True

    gravity =  500
    frame_rate = 60

    def exit_game(running):
        running = False
    pause_menu = create_pause_menu(screen, screen_width, screen_height, exit_game)
    pause_menu.disable()

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    non_player_sprites = pygame.sprite.Group()

    levels = pygame.sprite.Group()

    clock = pygame.time.Clock()


    backgroundSprite = background.Background(0,-10000+600)
    all_sprites.add(backgroundSprite)
    non_player_sprites.add(backgroundSprite)


    playerSprite = player.Player(levels,width,height,gravity, non_player_sprites)
    all_sprites.add(playerSprite)

    platform_array = [[250,320],[300,320]]

    for items in platform_array:
        platformSprite = platform.Platform(items[0],items[1])
        levels.add(platformSprite)
        all_sprites.add(platformSprite)
        non_player_sprites.add(platformSprite)

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause_menu.enable()
                    pause_menu.mainloop(screen)
                if event.key == K_UP:
                    playerSprite.accelerate(1)
                if event.key == K_DOWN:
                    playerSprite.accelerate(-1)


            if event.type == KEYUP:
                if event.key == K_UP:
                    playerSprite.accelerate(-1)
                if event.key == K_DOWN:
                    playerSprite.accelerate(1)
        
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[K_RIGHT]:
            playerSprite.rotate(1)
        if keys[K_LEFT]:
            playerSprite.rotate(-1)

        screen.fill((0,0,0))
        playerSprite.update(gravity, levels, non_player_sprites)
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()
        clock.tick(frame_rate)

    return