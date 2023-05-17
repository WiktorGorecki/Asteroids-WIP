import sys

import pygame

from button import Button
from config import config
from utils.get_font import get_font
from utils.settings import readSettings, writeSettings

def options(SCREEN):
    settings = readSettings()
    lastKeys = ["A","A","A","A","A"]
    while 1:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        # OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, config['TEXT_COLOR'])
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(
            pos=(640, 460),
            text_input="BACK",
            font=get_font(75)
        )

        if settings["fullscreen"]:
            toggletext ="WINDOWED"
        else:
            toggletext = "FULLSCREEN"

        OPTIONS_TOGGLE_FULLSCREEN = Button(
            pos=(640, 200),
            text_input=toggletext,
            font=get_font(30)
        )

        OPTIONS_SAVE_BUTTON = Button(
            pos=(640, 600),
            text_input="SAVE SETTINGS",
            font=get_font(30)
        )

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_TOGGLE_FULLSCREEN.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_SAVE_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_TOGGLE_FULLSCREEN.update(SCREEN)
        OPTIONS_SAVE_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    from screens.main_menu import main_menu
                    main_menu(SCREEN)
                if OPTIONS_TOGGLE_FULLSCREEN.checkForInput(OPTIONS_MOUSE_POS):
                    settings["fullscreen"] = not settings["fullscreen"]
                if OPTIONS_SAVE_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    writeSettings(settings)
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                lastKeys[0] = lastKeys[1]
                lastKeys[1] = lastKeys[2]
                lastKeys[2] = lastKeys[3]
                lastKeys[3] = lastKeys[4]
                lastKeys[4] = event.key
                if lastKeys[0]==pygame.K_b and lastKeys[1]==pygame.K_r and lastKeys[2]==pygame.K_o and lastKeys[3]==pygame.K_w and lastKeys[4]==pygame.K_n:
                    settings["brown_floyd"] = not settings["brown_floyd"]
                    writeSettings(settings)
                    print("Brown Floyd: "+str(settings["brown_floyd"]))
            pygame.display.update()