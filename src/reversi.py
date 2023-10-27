import copy 

UNKNOWN = 0
FIRST = 1
SECOND = 2
TIE = 3
BOARD_SIZE = 8


class reversi:
    def __init__(self) -> None:
        self.board = [[UNKNOWN for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] 
        self.current_player = FIRST
        self.set_winner = UNKNOWN

        mid = BOARD_SIZE // 2
        self.board[mid-1][mid-1] = self.board[mid][mid] = FIRST
        self.board[mid-1][mid] = self.board[mid][mid-1] = SECOND


    def can_move(self, x, y) -> bool: 
        #illegal move? 
        if x < 0 or x >= BOARD_SIZE: 
            return False 
        if y < 0 or y >= BOARD_SIZE: 
            return False 
        if self.board[x][y] != UNKNOWN: 
            return False

        for dx in [-1, 0, 1]: 
            for dy in [-1, 0, 1]: 
                if dx == 0 and dy == 0: 
                    continue
            
                #find next in direction... 
                xx = x + dx
                yy = y + dy
                while (0 <= xx < BOARD_SIZE) and (0 <= yy < BOARD_SIZE): 
                    #Wasn't assigned 
                    if self.board[xx][yy] == UNKNOWN: 
                        break 

                    #found a line to reverse
                    if self.board[xx][yy] == self.current_player: 
                        if (abs(xx - x) > 1 or abs(yy - y) > 1):
                            return True 
                        break 

                    xx += dx
                    yy += dy

        return False 


    def winner(self) -> int: 
        #Did a player violate the rules? 
        if self.set_winner != UNKNOWN: 
            return self.set_winner
        
        #can the current player move? 
        for i in range(BOARD_SIZE): 
            for j in range(BOARD_SIZE): 
                if self.can_move(i, j): return UNKNOWN
        
        #count who has more squares
        cf = cs = 0
        for l in self.board: 
            for v in l:
                if v == FIRST: 
                    cf += 1
                if v == SECOND: 
                    cs += 1

        if cf > cs: return FIRST
        if cf < cs: return SECOND
        return TIE 
            
    
    def turn(self) -> int: 
        return self.current_player


    def play(self, x, y) -> None: 
        #illegal move? 
        if not self.can_move(x, y): 
            self.set_winner = FIRST if self.current_player == SECOND else SECOND
            return 

        self.board[x][y] = self.current_player

        for dx in [-1, 0, 1]: 
            for dy in [-1, 0, 1]: 
                if dx == 0 and dy == 0: 
                    continue
            
                #find next in direction... 
                xx = x + dx
                yy = y + dy
                while (0 <= xx < BOARD_SIZE) and (0 <= yy < BOARD_SIZE): 
                    #Wasn't assigned 
                    if self.board[xx][yy] == UNKNOWN: 
                        break 

                    #found a line to reverse
                    if self.board[xx][yy] == self.current_player: 
                        while (xx != x or yy != y):
                            self.board[xx][yy] = self.current_player
                            xx -= dx
                            yy -= dy 
                        break

                    xx += dx
                    yy += dy

        self.current_player = SECOND if self.current_player == FIRST else FIRST


    def get_board(self) -> list[list[int]]:  
        return copy.deepcopy(self.board)