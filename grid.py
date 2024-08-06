import pygame
from colors import Colors

'''
Need functions that:
- Check if the row is filled - Check
- Clear the row if it's filled - Check
 - I don't think I need to initialise anything here.
    Loop through every row & column within the grid to check if it's filled
    For each row that is filled, remove the row entirely.
    Then move the row down
- Move the row down once it's cleared - Check
'''
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

    def is_row_filled(self, row):
        return all(self.grid[row])
    
    def insert_empty_row_at_the_top(self):
        empty_row = [0] * self.num_cols
        self.grid.insert(0, empty_row)

    def clear_row(self, row):
        self.grid.pop(row)
    
    def clear_row_move_down(self):
        for row in range(self.num_rows):
            if self.is_row_filled(row):
                self.clear_row(row)
                self.insert_empty_row_at_the_top()
                
    def reset(self):
        #Nested list comprehension might not work for this case.
        #self.grid = [[0 for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0                
                
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                  # Rect method to be drawn on the screen - Margins are added to acquire the 29 pixels
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size +11, 
                                        self.cell_size -1, self.cell_size-1) 
                # Draw method (acquires color tuple for that specific cell)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) 
                
#grid = Grid()
#grid.print_grid()

#grid.grid[0] = [1 for i in grid.grid[0]]
#print(grid.grid[0])
   
#grid.eliminate_filled_rows()
#print(grid.grid[0])
