from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
        
    #Randomly decides what block is used next
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)
    
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)
    
    def move_down(self):
        self.current_block.move(1 , 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, -0)
            self.lock_block()
    
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for pos in tiles:
            self.grid.grid[pos.row][pos.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_row_move_down()
        if rows_cleared > 0:
             self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True
    
    def block_fits(self): # Similar to block_inside but us
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                #print(f"Block does not fit at row {tile.row}, column {tile.column}")
                return False
        return True
                
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
    
    def hard_drop(self): # Should instantly move the current block down until it collides with the grid or the block below
        while True:
            # Moves the block down
            self.current_block.move(1,0)
            # Checks for collisions
            if self.block_inside() == False or self.block_fits() == False:
                # This moves the block back up by one row(undo the last move)
                self.current_block.move(-1, 0)
                break
            self.grid.clear_row_move_down()
            self.lock_block()
            break
               
    
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        #Checks if there are any tiles outisde of the grid
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def paused(self):
        pass
    
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        
        next_block_positions = {
            3: (255, 290),
            4: (255, 280)
        }
        default_position = (270, 270)
        
        next_position = next_block_positions.get(self.next_block.id, default_position)
        self.next_block.draw(screen, *next_position)
