#!/usr/bin/python3

from sprite import *
import pygame

def handle_events(char, SCREEN_WIDTH):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            x, y = char.rect.center
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                if x > 0:
                    char.setDirection('left')
                    char.image = pygame.image.load('include/char/char_walk_left.gif').convert()
                    char.image = pygame.transform.scale(char.image, (100, 100))
                    return (char)
            elif x < SCREEN_WIDTH - 70 and event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                char.setDirection('right')
                char.image = pygame.image.load('include/char/char_walk_right.gif').convert()
                char.image = pygame.transform.scale(char.image, (100, 100))
                return (char)
        char.setDirection('null')
    return(char)