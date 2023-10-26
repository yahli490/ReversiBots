import copy 

UNKNOWN = 0
FIRST = 1
SECOND = 2
TIE = 3
BOARD_SIZE = 8


class reversi:
    def __init__(self):
        self.board = [[UNKNOWN for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] 
        self.current_player = FIRST

        mid = BOARD_SIZE // 2
        self.board[mid-1][mid-1] = self.board[mid][mid] = FIRST
        self.board[mid-1][mid] = self.board[mid][mid-1] = SECOND


    def can_move(self): 
        return False #@TODO 


    def winner(self): 
        if self.can_move(): 
            return UNKNOWN
        
        cf = cs = 0
        for l in self.board: 
            for v in l:
                if v == FIRST: 
                    cf += 1
                if v == SECOND: 
                    cs += 1

        if cf > cs: 
            return FIRST
        
        if cf < cs: 
            return SECOND
        
        return TIE 
            
    
    def turn(self): 
        return self.current_player


    def play(self, x, y): 
        return #TODO 


    def board(self):  
        return copy.deepcopy(self.board)