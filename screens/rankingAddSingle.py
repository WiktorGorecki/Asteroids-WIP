import sys

import pygame

from button import Button
from utils.get_font import get_font

def rankingAddSingle(SCREEN, score):
    lastKeys = ["", "", ""]
    while 1:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("GAME OVER", True, "green")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SCORE_TEXT = get_font(45).render("YOUR SCORE:", True, "green")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(320, 250))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        NUMBER_TEXT = get_font(45).render(str(score), True, "green")
        NUMBER_RECT = NUMBER_TEXT.get_rect(center=(960, 250))
        SCREEN.blit(NUMBER_TEXT, NUMBER_RECT)

        INIT_TEXT = get_font(45).render("ENTER YOUR NAME:", True, "green")
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
        for i in range(0,3,1):
            initials+=lastKeys[i]

        NAME_TEXT = get_font(45).render(initials, True, "green")
        NAME_RECT = NAME_TEXT.get_rect(center=(960, 400))
        SCREEN.blit(NAME_TEXT, NAME_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.rankingScreenSingle import rankingScreenSingle
                    from utils.ranking import addHighScoreSingle
                    if len(initials) == 0:
                        initials = "NUL"
                    addHighScoreSingle(initials, score)
                    rankingScreenSingle(SCREEN)
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == "backspace":
                    lastKeys[0] = ""
                    lastKeys[1] = ""
                    lastKeys[2] = ""
                else:
                    lastKeys[0] = lastKeys[1]
                    lastKeys[1] = lastKeys[2]
                    keyName = pygame.key.name(event.key)
                    if keyName == "space":
                        keyName = " "
                    if keyName != "left ctrl" and keyName != "left alt" and keyName != "right ctrl" and keyName != "right alt" and keyName != "left meta" and keyName != "tab" and keyName != "left shift" and keyName != "right shift":
                        lastKeys[2] = keyName


        pygame.display.update()