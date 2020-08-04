import pygame
import os

#Window settings
WIDTH = 1280
HEIGHT = 720
TITLE = "Pokemon"

#Images
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('assets','background.png')), (WIDTH,HEIGHT))

