from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,  url_for, flash, redirect, request
import datetime

app = Flask(__name__) # Створюємо веб–додаток Flask
@app.route("/", methods = ["POST", "GET"]) # Вказуємо url-адресу для виклику функції
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5001, debug=True) # Запускаємо веб-сервер з цього файлу