#!/usr/bin/python3

from sprite import *
import pygame

def handle_movements(char, SCREEN_WIDTH):
    x, y = char.rect.center
    keys = pygame.key.get_pressed()
    
    if x > -35 and keys[pygame.K_LEFT]:
        char.setDirection('left')
        char.image = pygame.image.load('include/char/char_walk_left.gif').convert()
        char.image = pygame.transform.scale(char.image, (100, 100))
    elif x < SCREEN_WIDTH - 70 and keys[pygame.K_RIGHT]:
        char.setDirection('right')
        char.image = pygame.image.load('include/char/char_walk_right.gif').convert()
        char.image = pygame.transform.scale(char.image, (100, 100))
    char.update()

def handle_events(char, SCREEN_WIDTH):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            return False