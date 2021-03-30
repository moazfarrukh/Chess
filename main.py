import pygame 
from surfaces import *
from pieces import Pawn
BLACK = pygame.Color("#000000")
WHITE = pygame.Color("#FFFFFF")
pygame.init()
pygame.display.set_caption("test")
pawns = [Pawn(pawn,(80*i,80)) for i in range(8)]
black_pawns = [Pawn(black_pawn,(80*i,480)) for i in range(8)] 
def blit_pieces():
    window_surface.blit(black_rook,(0,560))
    window_surface.blit(black_knight,(80,560))
    window_surface.blit(black_bishop,(160,560))
    window_surface.blit(black_king,(240,560))
    window_surface.blit(black_queen,(320,560))
    window_surface.blit(black_bishop,(400,560))
    window_surface.blit(black_knight,(480,560))
    window_surface.blit(black_rook,(560,560))
    for i in range(8):
        window_surface.blit(black_pawns[i].surface,black_pawns[i].position)
        window_surface.blit(pawns[i].surface,pawns[i].position)

    window_surface.blit(rook,(0,0))
    window_surface.blit(knight,(80,0))
    window_surface.blit(bishop,(160,0))
    window_surface.blit(king,(240,0))
    window_surface.blit(queen,(320,0))
    window_surface.blit(bishop,(400,0))
    window_surface.blit(knight,(480,0))
    window_surface.blit(rook,(560,0))
    
is_running = True
while is_running :
    window_surface.fill(BLACK)
    window_surface.blit(image,(0,0))    
    blit_pieces()  

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w:
                pawns[2].move((pawns[2].position[0],pawns[2].position[1]-80))
            elif event.key == pygame.K_s:
                pawns[2].move((pawns[2].position[0],pawns[2].position[1]+80))
            elif event.key == pygame.K_d:
                pawns[2].move((pawns[2].position[0]+80,pawns[2].position[1]))
            elif event.key == pygame.K_a:
                pawns[2].move((pawns[2].position[0]-80,pawns[2].position[1]))
            print("changed")
    pygame.display.update()
