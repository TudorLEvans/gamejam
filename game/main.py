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

    gravity_constant =  100
    frame_rate = 60

    def exit_game(running):
        running = False
    pause_menu = create_pause_menu(screen, screen_width, screen_height, exit_game)
    pause_menu.disable()

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    non_player_sprites = pygame.sprite.Group()
    gravity_bodies = pygame.sprite.Group()

    clock = pygame.time.Clock()


    backgroundSprite = background.Background(0,600-60000)
    all_sprites.add(backgroundSprite)
    non_player_sprites.add(backgroundSprite)

    playerSprite = player.Player(screen_width, screen_height)
    all_sprites.add(playerSprite)

    moon = platform.Platform(0,-100000, -200, 1, True)
    gravity_bodies.add(moon)
    all_sprites.add(moon)
    non_player_sprites.add(moon)

    earth = platform.Platform(0,320, 300, 1.3, False)
    gravity_bodies.add(earth)
    all_sprites.add(earth)
    non_player_sprites.add(earth)


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
        playerSprite.update(gravity_constant, gravity_bodies, non_player_sprites)
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()
        clock.tick(frame_rate)

    return