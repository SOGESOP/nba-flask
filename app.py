from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
import pandas
import os
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///players.db"
app.app_context().push()
db=SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Players(db.Model):
    id=db.Column(db.Integer, primary_key=True) 
    name=db.Column(db.String(50),  unique=True)
    posistion=db.Column(db.String(2), nullable=False)
    age=db.Column(db.Integer, nullable=False)
    team=db.Column(db.String(3), nullable=False)
    games=db.Column(db.Integer)
    # games_started=db.Column(db.Integer)
    minutes_played=db.Column(db.Integer)
    # fg_made=db.Column(db.Integer)
    # fg_attempted=db.Column(db.Integer)
    fg_percent=db.Column(db.Integer)
    # three_point_made=db.Column(db.Integer)
    # three_point_attempt=db.Column(db.Integer)
    three_point_percent=db.Column(db.Integer)
    # two_point_made=db.Column(db.Integer)
    # two_point_attempted=db.Column(db.Integer)
    # two_point_percent=db.Column(db.Integer)
    # effective_fg=db.Column(db.Integer)
    # free_throw_made=db.Column(db.Integer)
    # free_throw_attempt=db.Column(db.Integer)
    free_throw_percent=db.Column(db.Integer)
    offensive_rb=db.Column(db.Integer)
    defensive_rb=db.Column(db.Integer)
    total_rb=db.Column(db.Integer)
    assist=db.Column(db.Integer)
    steals=db.Column(db.Integer)
    blocks=db.Column(db.Integer)
    turnover=db.Column(db.Integer)
    fouls=db.Column(db.Integer)
    points=db.Column(db.Integer)


    def __repr__(self):
        return '<Name %r>' %self.name
    
    
class InsertPlayer:
    def __init__(self, id, name, pos, age, team, g, mp,
                fgp, tpp, rb, ass, stl, blk, tur, fwl, pts ):
        self.id=id
        self.name-name
        self.pos=pos
        self.age=age
        self.team=team
        self.g=g
        self.mp=mp
        self.fgp=fgp
        self.tpp=tpp
        self.rb=rb
        self.ass=ass
        self.stl=stl
        self.blk=blk
        self.tur=tur
        self.fwl=fwl
        self.pts=pts

base_path=os.path.normpath({os.getcwd()}+ {os.sep}+ {os.pardir})
df_path=f"{base_path}{os.sep}static{os.sep}csv"

temp_df=pandas.read_csv(f"{df_path}{os.sep}2021.csv")

for i in range


@app.route("/")

def index():
    return render_template("index.html")


# can look up the error codes online

# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/players")

def players():
    return render_template("players.html")


