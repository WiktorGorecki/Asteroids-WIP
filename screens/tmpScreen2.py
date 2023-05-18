import sys

import pygame

from button import Button
from utils.get_font import get_font
from utils.stats import stats


def tmpScreen(SCREEN):
    stats['score'] = 0
    stats['healthpoints'] = 5

    while 1:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        SCORE_TEXT = get_font(25).render("SCORE:", True, "green")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(50, 50))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        NUMBER_TEXT = get_font(25).render(str(stats['score']), True, "green")
        NUMBER_RECT = NUMBER_TEXT.get_rect(center=(150, 50))
        SCREEN.blit(NUMBER_TEXT, NUMBER_RECT)

        heart = pygame.image.load('assets/heart.svg')
        for i in range(0, stats['healthpoints']):
            HEART_ICON = pygame.transform.scale(heart, (25, 25))
            HEART_RECT = HEART_ICON.get_rect(center=(50+i*25, 100))
            SCREEN.blit(HEART_ICON, HEART_RECT)

        if stats['healthpoints'] <= 0:
            from rankingAddDouble import rankingAddDouble
            rankingAddDouble(SCREEN, stats['score'])

        pygame.display.update()
