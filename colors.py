class Colors:
    dark_grey = (26, 31, 40)
    red = (232, 18, 18)
    green = (47, 230, 23)
    blue = (13, 64, 216)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls): #cls is referencing to the particular class
        return [cls.dark_grey, cls.red, cls.green, cls.blue, cls.orange, cls.yellow, cls.purple, cls.cyan]
