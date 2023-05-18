import sys

import pygame

import constants
from button import Button
from utils.get_font import get_font
from utils.settings import readSettings, writeSettings

def options(SCREEN):
    settings = readSettings()
    lastKeys = ["A","A","A","A","A"]
    while 1:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_BACK = Button(
            pos=(1100, 650), # Used to be 640, 460
            text_input="BACK",
            font=get_font(75)
        )
        font = get_font(40)
        displayModeText = font.render("Display Mode: ", True, constants.TEXT_COLOR)
        SCREEN.blit(displayModeText, (10,10))
        if settings["fullscreen"]:
            toggletext ="FULLSCREEN"
        else:
            toggletext = "WINDOWED"

        OPTIONS_TOGGLE_FULLSCREEN = Button(
            pos=(730, 30), # Used to be 640, 200 TODO: Center this button and the text behind it
            text_input=toggletext,
            font=get_font(40)
        )

        OPTIONS_SAVE_BUTTON = Button(
            pos=(640, 600),
            text_input="SAVE SETTINGS",
            font=get_font(40)
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