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
    
    def move_right(self):
        self.current_block.move(0, 1)
    
    def move_down(self):
        self.current_block.move(1 , 0)
    
    def move_rotate(self):
        self.current_block.rotate()
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
