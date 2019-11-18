from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    data = {"username":"jay_shen"}
    return render_template('index.html',title='Home',user=data)
