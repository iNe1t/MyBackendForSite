from flask import Flask, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")
@app.route("/articles")
def article_maker_page():
    return render_template("article.html")
if __name__ == "__main__":
    app.run(debug=True)