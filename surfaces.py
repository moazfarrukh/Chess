import pygame
import os
window_surface = pygame.display.set_mode((640,640))
image = pygame.image.load(os.path.join("assets","board.png"))
pieces = pygame.image.load(os.path.join("assets","pieces.png"))

pawn = pygame.Surface.subsurface(pieces,(420,0,80,80))
rook = pygame.Surface.subsurface(pieces,(340,0,80,80))
knight = pygame.Surface.subsurface(pieces,(250,0,80,80))
bishop = pygame.Surface.subsurface(pieces,(170,0,80,80))
king = pygame.Surface.subsurface(pieces,(84,0,80,80))
queen = pygame.Surface.subsurface(pieces,(0,0,80,80))
black_pawn = pygame.Surface.subsurface(pieces,(420,84,80,80))
black_rook = pygame.Surface.subsurface(pieces,(340,80,80,80))
black_knight = pygame.Surface.subsurface(pieces,(250,80,80,80))
black_bishop = pygame.Surface.subsurface(pieces,(170,80,80,80))
black_king = pygame.Surface.subsurface(pieces,(84,80,80,80))
black_queen = pygame.Surface.subsurface(pieces,(0,80,80,80))
