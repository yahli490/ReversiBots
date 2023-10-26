import os, secrets
import src.reversi as reversi


pass_len = 10
chr_options = "0123456789abcdefghijklmnopqrstuvwxyz" 
basedir = os.path.join("Submitted Code")
allowed_pass = []


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


def play_game(team, enemy): 
    #Isn't safe
    team = __import__(".".join([basedir, team]))
    enemy = __import__(".".join([basedir, enemy]))
    
    game = reversi.reversi()
    logs = []

    while game.winner() == reversi.UNKNOWN: 
        if game.turn() == reversi.FIRST: 
            x, y = team.get_move(game.board())
            game.play(x, y)
            logs.append([x, y])

        else: 
            x, y = enemy.get_move(game.board())
            game.play(x, y) 
            logs.append([x, y])

    return {"moves" : logs, "winner" : game.winner()}

    
    