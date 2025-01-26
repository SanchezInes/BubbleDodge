#!/usr/bin/python3

from sprite import *
from events import *
import pygame

def render_window(screen, clock, SCREEN_WIDTH):
    running = True
    texture = pygame.image.load('include/char/char_walk_left.gif').convert()
    texture = pygame.transform.scale(texture, (100, 100))
    char = sprite(100, 900, texture)

    while running:
        if handle_events(char, SCREEN_WIDTH) == False:
            running = False
        char = handle_events(char, SCREEN_WIDTH)
        screen.fill("purple")
        char.update()
        screen.blit(char.image, char.rect.center)
        pygame.display.flip()
        clock.tick(60)