import os, secrets, sys, multiprocessing
import src.reversi as reversi


pass_len = 10
chr_options = "0123456789abcdefghijklmnopqrstuvwxyz" 
basedir = os.path.join("Submitted Code")
allowed_pass = []
TIMEOUT = 0.42


#passcode -> path to python file
def pass_to_pyfile_path(passcode : str) -> str: 
    return os.path.join(basedir, passcode + ".py")


#Check that the passcode is true
def verify_user(passcode : str) -> bool: 
    return (passcode in allowed_pass)


#Check that the bot does exists 
def verify_exists(passcode : str) -> bool: 
    if not passcode.isalnum(): 
        return False
    
    return os.path.exists(pass_to_pyfile_path(passcode))


#upload a new python file 
def save_to_py_file(passcode : str, data : str) -> None: 
    if not os.path.exists(basedir): 
        os.makedirs(basedir)

    with open(pass_to_pyfile_path(passcode), "w") as f: 
        f.write(data)


#Generate passcodes for all users  
def generate_players(count : int) -> None: 
    if not os.path.exists(basedir): 
        os.makedirs(basedir)

    #Generate random passcodes and save them to passcodes.txt
    for _ in range(count): 
        new = "" 
        for i in range(pass_len): 
            new += chr_options[secrets.randbelow(len(chr_options))]
        allowed_pass.append(new)

    with open(os.path.join(basedir, "passcodes.txt"), "w") as f: 
        for pc in allowed_pass: 
            f.write(pc + "\n")


def proc_func(team, me, board, queue): 
    team = __import__(team); 
    x, y = team.get_move(me, board); 
    queue.put((x, y)) 


def child_proc_getmove(team, me, board): 
    queue = multiprocessing.Queue()
    my_proc = multiprocessing.Process(target=proc_func, args=(team, me, board, queue))
    
    my_proc.start()
    args = queue.get(timeout=TIMEOUT); 
    my_proc.kill()

    return args[0], args[1] 
    


def play_game(team, enemy):     
    if basedir not in sys.path: 
        sys.path.append(basedir)

    game = reversi.reversi()
    logs = []

    while game.winner() == reversi.UNKNOWN: 
        
        if any(game.can_move(i, j, reversi.FIRST) for i in range(reversi.BOARD_SIZE) for j in range(reversi.BOARD_SIZE)): 
            try: 
                x, y = child_proc_getmove(team, reversi.FIRST, game.get_board()); 
                game.play(x, y, reversi.FIRST)
                logs.append([x, y]) 
            except: 
                game.set_winner = reversi.SECOND

        if game.set_winner == reversi.UNKNOWN and any(game.can_move(i, j, reversi.SECOND) for i in range(reversi.BOARD_SIZE) for j in range(reversi.BOARD_SIZE)): 
            try: 
                x, y = child_proc_getmove(enemy, reversi.SECOND, game.get_board()); 
                game.play(x, y, reversi.SECOND) 
                logs.append([x, y])
            except: 
                game.set_winner = reversi.FIRST
                break 

    del team
    del enemy
    return {"moves" : logs, "winner" : game.winner()}

    
    