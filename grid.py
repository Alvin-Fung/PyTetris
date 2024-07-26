import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20 
        self.num_cols = 10
        self.cell_size = 30
        # Array to represent the grid itself
        self.grid = [[0 for i in range(self.num_cols)] for j in range (self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
            
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
        
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    '''
    Need functions that:
    - Check if the row is filled - Check
    - Clear the row if it's filled - Check
    - Move the row down once it's cleared
    '''
    
    def is_row_filled(self, row):
        is_filled = True
        for column in range(10):
            if self.grid[row][column] == 0:
                is_filled = False
        return is_filled
    
    '''
    Initialise a variable called lines_cleared to 0 - Check
    Loop for each row in the grid - Check
    If the row is "filled", returne True / Increment by 1(Might need do a double take on this one) - Check
    Remove the filled row from the grid. - Check(I think this is done right with the pop() method)
    Insert a new empty row at the top of the grid - I forgot I should initalise this first
    Increment lines_cleared by 1. - Check
    Return lines_cleared. - Check
    '''
    def clear_row(self):
        lines_cleared = 0
        new_grid = []
        for row in range(self.num_rows):
            if self.is_now_filled(row):
                # If the row is filled, increment lines_cleared
                lines_cleared += 1
            else: 
                # If the row is not filled, add it to the new grid(?)
                new_grid.append(row)
        return lines_cleared       
    
    '''
    I don't think I need to initialise anything here.
    For every row & column within the grid that is no longer filled, move it down
    '''
    
    def move_row_down(self):
        pass
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                  # Rect method to be drawn on the screen - Margins are added to acquire the 29 pixels
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, 
                                        self.cell_size -1, self.cell_size-1) 
                # Draw method (acquires color tuple for that specific cell)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) 
