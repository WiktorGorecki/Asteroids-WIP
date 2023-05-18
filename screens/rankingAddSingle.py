import sys

import pygame

from button import Button
from utils.get_font import get_font

def rankingAddSingle(SCREEN, score):
    lastKeys = ["", "", ""]
    while 1:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("GAME OVER", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SCORE_TEXT = get_font(45).render("YOUR SCORE:", True, "White")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(320, 250))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        NUMBER_TEXT = get_font(45).render(str(score), True, "White")
        NUMBER_RECT = NUMBER_TEXT.get_rect(center=(960, 250))
        SCREEN.blit(NUMBER_TEXT, NUMBER_RECT)

        INIT_TEXT = get_font(45).render("ENTER YOUR NAME:", True, "White")
        INIT_RECT = INIT_TEXT.get_rect(center=(320, 400))
        SCREEN.blit(INIT_TEXT, INIT_RECT)

        NEXT_BUTTON = Button(
            pos=(640, 550),
            text_input="NEXT",
            font=get_font(45)
        )

        NEXT_BUTTON.changeColor(PLAY_MOUSE_POS)
        NEXT_BUTTON.update(SCREEN)

        initials = ""
        for i in lastKeys:
            initials+=lastKeys[i]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.rankingScreenSingle import rankingScreenSingle
                    from utils.ranking import addHighScoreSingle
                    addHighScoreSingle(initials, score)
                    rankingScreenSingle(SCREEN)
            if event.type == pygame.KEYDOWN:
                if event.key == "Backspace":
                    lastKeys[0] = ""
                    lastKeys[1] = ""
                    lastKeys[2] = ""
                lastKeys[0] = lastKeys[1]
                lastKeys[1] = lastKeys[2]
                lastKeys[2] = event.key.key_code

        pygame.display.update()