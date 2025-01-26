#!/usr/bin/python3

import pygame

class sprite(pygame.sprite.Sprite):

    def __init__(self, x, y, texture):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.move_dir_x  = 0                        
        self.move_dir_y  = 0

    def update(self):
        x, y = self.rect.center
        x += self.move_dir_x
        self.rect.center = (x, y)

    def setDirection(self, dir):
        if (dir == 'left'):
            self.move_dir_x = -3
            self.move_dir_y = 0
        if (dir == 'right'):
            self.move_dir_x = 3
            self.move_dir_y = 0
        if (dir == 'null'):
            self.move_dir_x = 0
            self.move_dir_y = 0
