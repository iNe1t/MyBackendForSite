from flask import Flask, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def function():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)