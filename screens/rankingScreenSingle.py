import sys

import pygame

from button import Button
from utils.get_font import get_font
from utils.ranking import readRankingSingle, resetRankingSingle, rankingSingleLenghtCheck


def rankingScreenSingle(SCREEN):
    while 1:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("SINGLE HIGHSCORE TABLE", True, "green")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        rankingSingleLenghtCheck()
        table = readRankingSingle()
        for i in range(1,11,1):
            RANK_TEXT = get_font(20).render(str(i), True, "green")
            RANK_RECT = RANK_TEXT.get_rect(center=(320, 200+(i-1)*25))
            SCREEN.blit(RANK_TEXT, RANK_RECT)

            INIT_TEXT = get_font(20).render(table[str(i)]["initials"], True, "green")
            INIT_RECT = INIT_TEXT.get_rect(center=(640, 200 + (i - 1) * 25))
            SCREEN.blit(INIT_TEXT, INIT_RECT)

            SCORE_TEXT = get_font(20).render(str(table[str(i)]["score"]), True, "green")
            SCORE_RECT = SCORE_TEXT.get_rect(center=(960, 200 + (i - 1) * 25))
            SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        MENU_BUTTON = Button(
            pos=(300, 500),
            text_input="MAIN MENU",
            font=get_font(25)
        )

        RESET_BUTTON = Button(
            pos=(900, 500),
            text_input="RESET SCOREBOARD",
            font=get_font(25)
        )


        MENU_BUTTON.changeColor(PLAY_MOUSE_POS)
        MENU_BUTTON.update(SCREEN)

        RESET_BUTTON.changeColor(PLAY_MOUSE_POS)
        RESET_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.main_menu import main_menu
                    main_menu(SCREEN)
                if RESET_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.main_menu import main_menu
                    resetRankingSingle()
                    main_menu(SCREEN)

        pygame.display.update()
