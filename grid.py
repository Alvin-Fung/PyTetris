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
        print(self.grid)
            
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
    - Move the row down once it's cleared - In progress
    '''
    def is_row_filled(self, row):
        for column in range(10):
            if self.grid[row][column] == 0:
                return True
        return False
    
    def clear_row(self):  
     for row in self.grid:
         # All function checks to see if all items within a list are True
            if all(row) == True:
                for i in range(0,len(row)):
                    row[i] = 0
    
    '''
    I don't think I need to initialise anything here.
    Loop through every row & column within the grid to check if it's filled
    For each row that is filled, remove the row entirely.
    Then move the row down
    '''
    def remove_row(self, row):
        self.grid.pop(row)
    
    def move_row_down(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                if self.is_now_filled(row):
                    self.remove_row(row)
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                  # Rect method to be drawn on the screen - Margins are added to acquire the 29 pixels
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, 
                                        self.cell_size -1, self.cell_size-1) 
                # Draw method (acquires color tuple for that specific cell)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) 
                
#grid = Grid()
#grid.print_grid()

#grid.grid[0] = [1 for i in grid.grid[0]]
#print(grid.grid[0])
   
#grid.eliminate_filled_rows()
#print(grid.grid[0])
