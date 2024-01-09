from block import Block
from position import Position

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            #Rotation State 0, ...,...
            0: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(0,1), Position(0,1), Position(0,1)],
            2: [Position(0,1), Position(0,1), Position(0,1), Position(0,1)],
            3: [Position(0,1), Position(0,1), Position(0,1), Position(0,1)]
        }
