from flask import render_template
from app import app

@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/temperature_prediction")
def prediction():
    return render_template("/prediction.html")
