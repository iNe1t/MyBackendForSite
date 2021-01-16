from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return "Vova is a debil"

if __name__ == "__main__":
    app.run(debug=True)