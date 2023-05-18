import sys

import pygame

from button import Button
from utils.get_font import get_font

def rankingAddDouble(SCREEN, score):
    lastKeys = ["", "", "", "", "", ""]
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

        INIT1_TEXT = get_font(45).render("PLAYER 1:", True, "green")
        INIT1_RECT = INIT1_TEXT.get_rect(center=(320, 400))
        SCREEN.blit(INIT1_TEXT, INIT1_RECT)

        INIT2_TEXT = get_font(45).render("PLAYER 2:", True, "green")
        INIT2_RECT = INIT2_TEXT.get_rect(center=(320, 450))
        SCREEN.blit(INIT2_TEXT, INIT2_RECT)

        NEXT_BUTTON = Button(
            pos=(640, 600),
            text_input="NEXT",
            font=get_font(45)
        )

        NEXT_BUTTON.changeColor(PLAY_MOUSE_POS)
        NEXT_BUTTON.update(SCREEN)

        initials1 = ""
        for i in range(0,3,1):
            initials1+=lastKeys[i]

        initials2 = ""
        for i in range(3,6,1):
            initials2 += lastKeys[i]

        NAME1_TEXT = get_font(45).render(initials1, True, "green")
        NAME1_RECT = NAME1_TEXT.get_rect(center=(960, 400))
        SCREEN.blit(NAME1_TEXT, NAME1_RECT)

        NAME2_TEXT = get_font(45).render(initials2, True, "green")
        NAME2_RECT = NAME2_TEXT.get_rect(center=(960, 450))
        SCREEN.blit(NAME2_TEXT, NAME2_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    from screens.rankingScreenDouble import rankingScreenDouble
                    from utils.ranking import addHighScoreDouble
                    if len(initials1) == 0:
                        initials1 = "NUL"
                    if len(initials2) == 0:
                        initials2 = "NUL"
                    addHighScoreDouble(initials1, initials2, score)
                    rankingScreenDouble(SCREEN)
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == "backspace":
                    lastKeys[0] = ""
                    lastKeys[1] = ""
                    lastKeys[2] = ""
                    lastKeys[3] = ""
                    lastKeys[4] = ""
                    lastKeys[5] = ""
                else:
                    lastKeys[0] = lastKeys[1]
                    lastKeys[1] = lastKeys[2]
                    lastKeys[2] = lastKeys[3]
                    lastKeys[3] = lastKeys[4]
                    lastKeys[4] = lastKeys[5]
                    keyName = pygame.key.name(event.key)
                    if keyName == "space":
                        keyName = " "
                    if keyName != "left ctrl" and keyName != "left alt" and keyName != "right ctrl" and keyName != "right alt" and keyName != "left meta" and keyName != "tab" and keyName != "left shift" and keyName != "right shift":
                        lastKeys[5] = keyName


        pygame.display.update()