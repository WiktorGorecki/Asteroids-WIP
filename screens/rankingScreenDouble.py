import sys

import pygame

from button import Button
from utils.get_font import get_font
from utils.ranking import readRankingDouble, writeRankingDouble, rankingDoubleLenghtCheck, resetRankingDouble


def rankingScreenDouble(SCREEN, gamemode):
    while 1:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("HIGHSCORE TABLE", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        highscoretable = readRankingDouble()
        for i in range(1,11,1):
            RANK_TEXT = get_font(45).render(str(highscoretable[i][y]), True, "White")
            RANK_RECT = RANK_TEXT.get_rect(center=(200+y*300, 160+i*50))
            SCREEN.blit(RANK_TEXT, RANK_RECT)

        MENU_BUTTON = Button(
            pos=(640, 500),
            text_input="MAIN MENU",
            font=get_font(75)
        )


        MENU_BUTTON.changeColor(PLAY_MOUSE_POS)
        MENU_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.main_menu import main_menu
                    main_menu(SCREEN)

        pygame.display.update()