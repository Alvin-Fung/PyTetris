import pygame
import sys
from grid import Grid
import random


# Game loop
pygame.init()
dark_blue = (44, 44, 127)
screen = pygame.display.set_mode((300, 600)) # Width, Height
pygame.display.set_caption("Alvin's Tetris made in Python!")
clock = pygame.time.Clock()
running = True

game_grid = Grid()
game_grid.print_grid()

while running:
    for event in pygame.event.get():
        # pygame.QUIT event allows the user to click X to close the game window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    # Game Rendering/Drawing
    screen.fill(dark_blue)
    
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


