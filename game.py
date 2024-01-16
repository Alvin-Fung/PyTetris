from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = []
        self.current_block = [IBlock(), JBlock(), LBlock(), SBlock(), TBlock(), ZBlock()]
        self.next_block = self.get_random_block()
        
    #Randomly decides what block is used next
    def get_random_block(self):
        if self.blocks == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
        
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
