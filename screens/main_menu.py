import sys

import pygame

from button import Button
# from screens.game_mode import game_mode
from screens.options import options
from utils.get_font import get_font
# from config import config


def multiplayer(SCREEN):
    pass



def main_menu(SCREEN):
    while 1:
        SCREEN.fill('black')

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        logo = pygame.image.load('assets/logoroid.svg')
        MENU_LOGO = pygame.transform.scale(logo, (580, 580))
        MENU_RECT = MENU_LOGO.get_rect(center=(850, 350))

        SINGLEPLAYER_BUTTON = Button(pos=(640, 300), text_input="SINGLEPLAYER", font=get_font(75))
        MULTIPLAYER_BUTTON = Button(pos=(640, 420), text_input="MULTIPLAYER", font=get_font(75))
        RANKING_BUTTON = Button(pos=(640, 540), text_input="RANKING", font=get_font(75))
        SETTINGS_BUTTON = Button(pos=(320, 660), text_input="SETTINGS", font=get_font(75))
        QUIT_BUTTON = Button(pos=(960, 660), text_input="QUIT", font=get_font(75))

        SCREEN.blit(MENU_LOGO, MENU_RECT)

        for button in [SINGLEPLAYER_BUTTON, MULTIPLAYER_BUTTON, RANKING_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SINGLEPLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from game import Game
                    game = Game(SCREEN)
                    game.main_loop(SCREEN)
                if MULTIPLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    multiplayer(SCREEN)
                if RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from screens.rankingScreenMain import rankingScreenMain
                    rankingScreenMain(SCREEN)
                if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(SCREEN)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
