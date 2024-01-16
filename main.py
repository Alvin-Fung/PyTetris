import pygame,sys
from grid import Grid
from blocks import *


# Game loop
pygame.init()
dark_blue = (44, 44, 127)
screen = pygame.display.set_mode((300, 600)) # Width, Height
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
running = True

game_grid = Grid()
#Test here to see if different colours show up on the grid

block = LBlock()
block.move(4,3)

while running:
    for event in pygame.event.get():
        # pygame.QUIT event allows the user to click X to close the game window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    # Game Rendering/Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # Limits the game to run at 60 FPS.
    

