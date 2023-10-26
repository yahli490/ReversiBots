from flask import Flask, render_template, request
import lib.server_utils as server_utils
import os 


players_count = 5
app = Flask(__name__, static_folder = os.path.join('templates', 'style'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/submit", methods=['GET'])
def submit_page(): 
    return render_template("submit.html")


@app.route("/submit", methods=['POST'])
def submit_code(): 
    passcode = request.form.get("passcode")
    if not server_utils.verify_user(passcode): 
        return "Incorrect passcode" 

    python = request.form.get("python")
    server_utils.save_to_py_file(passcode, python)

    return "Greate success!"
    

@app.route("/run", methods=["GET"])
def run_page(): 
    return render_template("run.html")


@app.route("/run", methods=["POST"])
def run_sim(): 
    team = request.form.get("team")
    enemy = request.form.get("enemy") 

    if not server_utils.verify_exists(team): 
        return "Wrong team!" 
    
    if not server_utils.verify_exists(enemy): 
        return "Wrong enemy!"

    #@TODO: simulate a game and return the logs. 
    return "Greate success!"


if __name__ == "__main__":
    server_utils.generate_players(players_count)
    app.run()