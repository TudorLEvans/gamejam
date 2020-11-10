import pygame
import pygame_menu
from game import main
from pygame_menu import themes
from .end_game import end_game_menu

mytheme = themes.Theme(
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    widget_font = pygame_menu.font.FONT_8BIT,
    title_font = pygame_menu.font.FONT_8BIT,
    title_offset=(20,20),
    background_color = (0,0,0),
    title_font_size = 30,
    menubar_close_button = False
)

def main_menu(screen, screen_width, screen_height):

    def start_game():
        win = main.mainGame(screen, screen_width, screen_height)
        if win != None:
            end_menu = end_game_menu(screen, screen_width, screen_height, start_game, win)
            end_menu.mainloop(screen)
        return

    menu = pygame_menu.Menu(
        screen_width, 
        screen_height, 
        'Fly me to the moon',
        theme=mytheme
    )
    
    menu.add_button('Play', start_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)