from block import Block
from position import Position

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            #Rotation State 0, ...,...
            0: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
            3: [Position(0,0), Position(0,1), Position(1,1), Position(2,1)]
        }

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells ={
            0: [Position(), Position(), Position(), Position()],
            1: [Position(), Position(), Position(), Position()],
            2: [Position(), Position(), Position(), Position()],
            3: [Position(), Position(), Position(), Position()]
        }
        
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells ={
            0: [Position(), Position(), Position(), Position()],
            1: [Position(), Position(), Position(), Position()],
            2: [Position(), Position(), Position(), Position()],
            3: [Position(), Position(), Position(), Position()]
        }

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells ={
            0: [Position(), Position(), Position(), Position()],
            1: [Position(), Position(), Position(), Position()],
            2: [Position(), Position(), Position(), Position()],
            3: [Position(), Position(), Position(), Position()]
        }

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells ={
            0: [Position(), Position(), Position(), Position()],
            1: [Position(), Position(), Position(), Position()],
            2: [Position(), Position(), Position(), Position()],
            3: [Position(), Position(), Position(), Position()]
        }

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells ={
            0: [Position(), Position(), Position(), Position()],
            1: [Position(), Position(), Position(), Position()],
            2: [Position(), Position(), Position(), Position()],
            3: [Position(), Position(), Position(), Position()]
        }
