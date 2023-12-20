class Grid:
    def __init__(self):
        self.num_rows = 20 
        self.num_cols = 10
        self.cell_size = 30
        # Array to represent the grid itself
        self.grid = [[0 for i in range(self.num_cols)] for j in range (self.num_rows)]
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
            
    def get_cell_colors(self):
        
        dark_grey = (26, 31, 40)
        red = (232, 18, 18)
        green = (47, 230, 23)
        blue = (13, 64, 216)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        
        return [dark_grey, red, green, blue, orange, yellow, purple, cyan]

    def draw(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
