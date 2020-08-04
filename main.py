import pygame
import os
import time
import random
from const import WIDTH, HEIGHT, TITLE, BACKGROUND_IMAGE


pygame.font.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)



def main():
    """
        Function    : main function of application
        Description : mainloop of application
        Parameters  : None
        Return      : None
        Examples of Usage:
            self.main()
        """
    run = True
    FPS = 60
    main_font = pygame.font.SysFont('comicsans', 50)
    clock = pygame.time.Clock()
    
    def redraw_window():
        """
        Function    : function for drawing content
        Description : redraws all componets of window
        Parameters  : None
        Return      : None
        Examples of Usage:
            self.redraw_window()
        """
        SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()
        