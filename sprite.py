#!/usr/bin/python3

import pygame

class sprite(pygame.sprite.Sprite):

    def __init__(self, x, y, texture):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.move_dir_x  = x                        
        self.move_dir_y  = y

    def update(self):
        self.rect.center = (self.move_dir_x, self.move_dir_y)

    def setDirection(self, dir):
        if (dir == 'left'):
            self.move_dir_x -= 3
            self.move_dir_y = self.move_dir_y
        if (dir == 'right'):
            self.move_dir_x += 3
            self.move_dir_y = self.move_dir_y
