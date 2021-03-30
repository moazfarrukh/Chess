import pygame
class Pawn():
    def __init__(self,surface,position) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.position = position
        self.dim = self.surface
    def move(self,new_cords):
        self.position =  new_cords
