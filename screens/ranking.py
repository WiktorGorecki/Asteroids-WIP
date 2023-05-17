import sys

import pygame

from button import Button
from utils.get_font import get_font


def ranking(SCREEN, gamemode):
    while 1:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("This is the RANKING screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        MENU_BUTTON = Button(
            pos=(640, 460),
            text_input="MAIN MENU",
            font=get_font(75)
        )


        #RANKING_NAME_INPUT = pygame.Rect(200, 200, 140, 32)


        RANKING_NAME_INPUT = Button(
            pos=(640, 300),
            text_input="RANKING",
            font=get_font(75)
        )


        MENU_BUTTON.changeColor(PLAY_MOUSE_POS)
        MENU_BUTTON.update(SCREEN)

        RANKING_NAME_INPUT.changeColor(PLAY_MOUSE_POS)
        RANKING_NAME_INPUT.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.main_menu import main_menu
                    main_menu(SCREEN)
                if RANKING_NAME_INPUT.checkForInput(PLAY_MOUSE_POS):
                    from screens.rankingShow import rankingSHOW
                    rankingSHOW(SCREEN, gamemode)

        pygame.display.update()
