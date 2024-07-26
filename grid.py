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
    - Check if the row is filled
    - Clear the row if it's filled
    - Move the row down once it's cleared
    '''
    
    def is_row_filled(self, row):
        is_filled = True
        for column in range(10):
            if self.grid[row][column] == 0:
                is_filled = False
        return is_filled
    
    def clear_row(self):
        pass
    
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
