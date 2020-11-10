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
from .sprites import platform, player, background, score_tracker, speedometer, timer
from menu.pause import create_pause_menu

def mainGame(screen, screen_width, screen_height):

    gravity_constant =  100
    frame_rate = 60
    journey_length = 100000

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

    moon = platform.Platform(0,-journey_length + screen_height/2, -200, 1, True, "moon")
    gravity_bodies.add(moon)
    all_sprites.add(moon)
    non_player_sprites.add(moon)

    earth = platform.Platform(0,320, 300, 1.3, False, "earth")
    gravity_bodies.add(earth)
    all_sprites.add(earth)
    non_player_sprites.add(earth)

    speedometerSprite = speedometer.Speedometer(screen_height)
    all_sprites.add(speedometerSprite)

    timerSprite = timer.Timer(screen_width, screen_height)
    all_sprites.add(timerSprite)

    scoreSprite = score_tracker.Score(journey_length)
    all_sprites.add(scoreSprite)

    def main_game_loop():
        global running
        running = True
        global gamePaused
        gamePaused = False
        global win
        win = None

        time = 0
        while running:
            time += clock.get_time()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        gamePaused = True
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
            
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT]:
                playerSprite.rotate(1)
            if keys[K_LEFT]:
                playerSprite.rotate(-1)

            screen.fill((0,0,0))

            win = playerSprite.update(screen_width, gravity_constant, gravity_bodies, non_player_sprites)

            if win != None:
                running = False

            scoreSprite.update_score(screen_width, journey_length, journey_length + moon.rect.centery)
            speedometerSprite.update_speed(screen_height, playerSprite.v_y)
            timerSprite.update_time(screen_width, screen_height, time)

            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)

            pygame.display.flip()
            clock.tick(frame_rate)

    pause_menu = create_pause_menu(screen, screen_width, screen_height, main_game_loop)
    pause_menu.disable()

    main_game_loop()

    print(gamePaused)

    if gamePaused:
        pause_menu.enable()
        pause_menu.mainloop(screen)

    return win