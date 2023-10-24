from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/submit", methods=['GET'])
def submit_page(): 
    return render_template("submit.html")


@app.route("/submit", methods=['POST'])
def submit_code(): 
    passcode = request.form.get("passcode")
    #TODO: verify passcode;  
    python = request.form.get("python")
    #TODO: save file; 
    print(passcode, python)
    return "Greate success!"
    

@app.route("/run")
def run_sim(): 
    return render_template("run.html")


if __name__ == "__main__":
    app.run()