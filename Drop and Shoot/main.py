import pygame, sys, os
from pygame.locals import *

dir(pygame)

pygame.init()

window = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Drop and Shoot")

screen = pygame.display.get_surface()

#images needed are wheels that rotate, rig, explosion, explosive rock, rock, background
#music needed are moving, explosion noise and reload

running = True
