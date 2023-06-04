from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,  url_for, flash, redirect, request
import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__) # Створюємо веб–додаток Flask
db = SQLAlchemy() # створюємо  БД
app.config['SECRET_KEY'] = "680581c5172841f87212bf4f927279ef4c860f9c"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///client.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False, nullable=False)
    number = db.Column(db.String(50))

@app.route("/", methods = ["POST", "GET"]) # Вказуємо url-адресу для виклику функції
def index():
    if request.method == "POST":    
        user = User(username=request.form['name'], number=request.form['phone'])
        db.session.add(user)    
        db.session.commit()

    return render_template("index.html")

@app.route("/service", methods = ["POST", "GET"]) # Вказуємо url-адресу для виклику функції
def service():
    return render_template("service.html")

# if __name__ == "__main__":
#     app.config['TEMPLATES_AUTO_RELOAD'] = True
#     app.run(port=5001, debug=True) # Запускаємо веб-сервер з цього файлу

# with app.app_context():
#     db.create_all()
#     user = User(username='vikf', number='098888f')
#     db.session.add(user)
#     db.session.commit()
