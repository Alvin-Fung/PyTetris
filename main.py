import pygame
import sys
from grid import Grid
import random


# Game loop
pygame.init()
dark_blue = (44, 44, 127)
screen = pygame.display.set_mode((300, 600)) # Width, Height
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()
running = True

game_grid = Grid()
#Testing to see if different colours show up on the grid
game_grid.grid[0][0] = 1 
game_grid.grid[3][5] = 4 
game_grid.grid[17][8] = 7 

game_grid.print_grid()

while running:
    for event in pygame.event.get():
        # pygame.QUIT event allows the user to click X to close the game window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    # Game Rendering/Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # Limits the game to run at 60 FPS.
    
# Global Variables
blockSize = 30

# Shape Formats
S = [[
    ['.....',
     '.....',
     '0000.',
     '.....',
     ],
    ['.....',
     '..0..',
     '..0..',
     '..0..',
     '..0..',
    ],
    [
    ['.....',
     '.....',
     '..0..',
     '.000.',
     '.....'],
    ['.....',
     '..0..',
     '.00..',
     '..0..'
     '.....'],
    ['.....',
     '.....',
     '.000.',
     '..0..',
     '.....',],
    [
     '.....',
     '..0..',
     '..00.',
     '..0..',
     '.....',]
    ],
    [
      ['.....',
       '.....',
       '..00.',
       '.00..',
       '.....'],
      ['.....',
       '.....',
       '.00..',
       '..00.',
       '.....',],
      ['.....',
       '.0...',
       '.00..',
       '..0..',
       '.....',],
      ['.....',
       '..0..',
       '.00..',
       '.0...',
       '.....',], 
    ],
    [
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....',],
     ['.....',
      '...0.',
      '.000.',
      '.....',
      '.....',],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....',],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....',]
    ],
    [
     ['.....',
      '.000.',
      '.000.',
      '.....',
      '.....',]   
    ]
]]


