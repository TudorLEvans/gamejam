import pygame
import pygame_menu
from game import main

def main_menu(screen,width,height):
    def start_game():
        main.mainGame(screen,width,height)
    menu = pygame_menu.Menu(300, 400, 'Welcome',
                        theme=pygame_menu.themes.THEME_BLUE)

    menu.add_text_input('Name : ', default='Tudor?')
    menu.add_button('Play', start_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)