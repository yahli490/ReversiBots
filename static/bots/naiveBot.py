import src.reversi as reversi 


def get_move(me, board): 
    #get a reversi object. 
    game = reversi.reversi()
    game.current_player = me
    game.board = board 

    for i in range(reversi.BOARD_SIZE): 
        for j in range(reversi.BOARD_SIZE): 
            if game.can_move(i, j): 
                return i, j 
