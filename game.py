from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        
    #Randomly decides what block is used next
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False:
            self.current_block.move(0, 1)
    
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False:
            self.current_block.move(0, -1)
    
    def move_down(self):
        self.current_block.move(1 , 0)
        if self.block_inside() == False:
            self.current_block.move(-1, -0)
    
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside == False:
            #Need rotation logic first but going to leave this as it is for now.
            pass
    
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        #Checks if there are any tiles outisde of the grid
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
