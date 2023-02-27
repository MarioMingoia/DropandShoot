import pygame, sys, os
from pygame.locals import *
import random

dir(pygame)

pygame.init()

class Boulder(sprite):
    def __init__(self, x, y, speed, screen):
        super(Boulder, self).__init__()
        self.x = random.randrange()
        self.y = random.randrange()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.speed = random.randrange(0.5, 1.5)

    def update():
        self.y += self.speed

        if self.y >= self.screen_rect.bottom:
            #game over
