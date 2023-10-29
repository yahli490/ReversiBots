# Example reversi bot.

# A function to return your next move.
# 'board' is a 8x8 int array, with 0 being an empty cell and 1,2 being you and the opponent,
# determained by the input 'me'.
def get_move(me : int, board : list[list[int]]) -> tuple[int]:
    for i in range(8): 
        for j in range(8): 
            if valid_move(i, j, me, board):
                return i, j 
    
    # if there is no valid move, the bot will never be called in the first place. For safety, we return an invalid result.
    return -1, -1


def valid_move(i, j, me, board):
    #TODO: implement
    pass


