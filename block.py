from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
        
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
        
    #This method will return the occupied positions with the offset applied in a list
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state] #Default cell position
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        # All blocks other than the square block has 4 rotation states
        if self.rotation == len(self.cells): # This resets the rotation state after the final increment
            self.rotation_state = 0
    
    def draw(self, screen):
        tiles = self.get_cell_positions() #Retrieves the current position of the rotation state
        for tile in tiles:
            # Similar to what we did in the grid class to offeset 1 pixel
            tile_rect = pygame.Rect(tile.column * self.cell_size +1, tile.row * self.cell_size +1, 
                                    self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect) 
