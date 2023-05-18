import pygame

from stats import stats

def scoreHandler(input):
    if input=='onAsteroidHit':
        stats['score'] += 1
    if input=='smallAsteroidDestroyed':
        stats['score'] += 1
    if input=='mediumAsteroidDestroyed':
        stats['score'] += 5
    if input=='bigAsteroidDestroyed':
        stats['score'] += 10

    if input=='onShipHit':
        stats['healthPoints'] -= 1