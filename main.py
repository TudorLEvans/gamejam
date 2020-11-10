from menu import main
import pygame

size = screen_width, screen_height = 600, 600

pygame.init()

screen = pygame.display.set_mode(size)

moon_image, earth_image, player_image = pygame.image.load("images/moon.png"), pygame.image.load("images/earth.png"), pygame.image.load("images/rocket.png")


main.main_menu(screen, screen_width, screen_height, moon_image, earth_image, player_image)