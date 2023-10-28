import src.reversi as reversi
import random


def distance_to_corner(x, y, game_size):
    return min(x, game_size - 1 - x) + min(y, game_size - 1 - y)


def get_move(me, board):
    #get a reversi object.
    game = reversi.reversi()
    game.current_player = me
    game.board = board

    min_distance = reversi.BOARD_SIZE
    min_locations = []
    for i in range(reversi.BOARD_SIZE):
        for j in range(reversi.BOARD_SIZE):
            if game.can_move(i, j, me):
                dis = distance_to_corner(i, j, reversi.BOARD_SIZE)
                if dis < min_distance:
                    min_distance = dis
                    min_locations = [(i, j)]
                elif dis == min_distance:
                    min_locations.append((i, j))
    if len(min_locations) == 0:
        return 0, 0
    return random.choice(min_locations)