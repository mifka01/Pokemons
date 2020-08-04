import pygame
from trainer import Trainer

class Player(Trainer):
    """
    Player class
    Inherits from Trainer
    Parameters
    ----------
    name: name of player / trainer,
    x_pos: x position on game screen
    y_pos: y position on game screen
    Description
    ----------
    Main class of player in game
    """
    def __init__(self, name: str, x_pos: int, y_pos: int):
        super().__init__(name=name, x_pos=x_pos, y_pos=y_pos)
        self.mask = pygame.mask.from_surface(self.trainer_image)

    def draw(self, window):
        """
        Function    : draw player on game window
        Parameters  : self, window: surface
        Return      : None
        Examples of Usage:
            self.draw(window: surface)
        """
        window.blit(self.trainer_image, (self.x_pos, self.y_pos))



