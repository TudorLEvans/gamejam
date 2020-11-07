import pygame
import pygame_menu
from game import main
from pygame_menu import themes

mytheme = themes.Theme(
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    widget_font = pygame_menu.font.FONT_8BIT,
    title_font = pygame_menu.font.FONT_8BIT,
    title_offset=(20,20),
    background_color = (0,0,0),
    title_font_size = 30,
    menubar_close_button = False
)

def create_pause_menu(screen, screen_width, screen_height, main_game_loop):

    pause_menu = pygame_menu.Menu(
        screen_width, 
        screen_height, 
        'Fly me to the moon',
        theme=mytheme
    )

    pause_menu.add_button('Return to Game', main_game_loop)
    pause_menu.add_button('Main Menu', pause_menu.disable)
    pause_menu.add_button('Quit', pygame_menu.events.EXIT)
    return pause_menu