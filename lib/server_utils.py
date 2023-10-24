import os, secrets

pass_len = 10
chr_options = "0123456789abcdefghijklmnopqrstuvwxyz" 
basedir = "Submitted Code"
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
