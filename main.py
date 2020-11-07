from menu import main
import pygame

size = screen_width, screen_height = 600, 600

pygame.init()

screen = pygame.display.set_mode(size)

main.main_menu(screen, screen_width, screen_height)