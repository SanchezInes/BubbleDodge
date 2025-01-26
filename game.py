#!/usr/bin/python3

import pygame
from render_window import *

def main():
    pygame.init()
    SCREEN_WIDTH = 650
    SCREEN_HEIGHT = 1100
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    render_window(screen, clock, SCREEN_WIDTH)
    pygame.quit()
    return(0)

main()