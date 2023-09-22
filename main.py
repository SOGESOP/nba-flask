from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///teams.db"

db=SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Teams(db.Model):
    id=db.Column(db.Integer, primary_key=True) 
    name=db.Column(db.String(50),  unique=True)
    record=db.Column(db.String(10 ))
    wins=db.Column(db.String(10))
    losses=db.Column(db.String(10))
    offensive_rating=db.Column(db.Integer)
    defensive_rating=db.Column(db.Integer)

    def __repr__(self):
        return '<Name %r>' %self.name
    
    
    db create all not working







@app.route("/")

def index():
    return render_template("index.html")


# can look up the error codes online

# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/teams")

def teams():
    return render_template("teams.html")


