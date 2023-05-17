import sys

import pygame

from button import Button
from utils.get_font import get_font


def rankingScreenMain(SCREEN):
    while 1:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("This is the RANKING screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        BACK_BUTTON = Button(
            pos=(640, 400),
            text_input="BACK",
            font=get_font(75)
        )


        RANKING_SINGLE_BUTTON = Button(
            pos=(640, 200),
            text_input="RANKING SINGLE",
            font=get_font(75)
        )

        RANKING_DOUBLE_BUTTON = Button(
            pos=(640, 300),
            text_input="RANKING DOUBLE",
            font=get_font(75)
        )


        BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        RANKING_SINGLE_BUTTON.changeColor(PLAY_MOUSE_POS)
        RANKING_SINGLE_BUTTON.update(SCREEN)

        RANKING_DOUBLE_BUTTON.changeColor(PLAY_MOUSE_POS)
        RANKING_DOUBLE_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.main_menu import main_menu
                    main_menu(SCREEN)
                if RANKING_SINGLE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.rankingShow import rankingSHOW
                    rankingSHOW(SCREEN, gamemode)

        pygame.display.update()
