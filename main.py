from menu import main
import pygame

size = width, height = 600, 600

pygame.init()

screen = pygame.display.set_mode(size)

main.main_menu(screen, width, height)