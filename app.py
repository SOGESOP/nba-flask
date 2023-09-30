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

class Players(db.Model):
    id=db.Column(db.Float, primary_key=True, autoincrement=True, nullable=True) 
    name=db.Column(db.String(50))
    pos=db.Column(db.String(2))
    age=db.Column(db.Float)
    tm=db.Column(db.String(3))
    g=db.Column(db.Float)
    gs=db.Column(db.Float)
    mp=db.Column(db.Float)
    fg=db.Column(db.Float)
    fga=db.Column(db.Float)
    fg_percent=db.Column(db.Float)
    three_point=db.Column(db.Float)
    three_point_a=db.Column(db.Float)
    three_point_percent=db.Column(db.Float)
    two_point=db.Column(db.Float)
    two_point_a=db.Column(db.Float)
    two_point_percent=db.Column(db.Float)
    efg=db.Column(db.Float)
    ft=db.Column(db.Float)
    fta=db.Column(db.Float)
    ft_percent=db.Column(db.Float)
    orb=db.Column(db.Float)
    drb=db.Column(db.Float)
    trb=db.Column(db.Float)
    ast=db.Column(db.Float)
    stl=db.Column(db.Float)
    blk=db.Column(db.Float)
    tov=db.Column(db.Float)
    pf=db.Column(db.Float)
    pts=db.Column(db.Float)


    def __repr__(self):
        return '<Name %r>' %self.name
    
with app.app_context():
    db.create_all()
    
    
class ReadCsv:
    def __init__(self) -> None:
        base_path=os.path.normpath(os.getcwd()+ os.sep+ os.pardir)
        df_path=f"{base_path}{os.sep}nba-flask{os.sep}static{os.sep}csv"
        global temp_df
        temp_df=pandas.read_csv(f"{df_path}{os.sep}2021.csv")
        for i in range(0, len(temp_df["Player"])):
            entry=Players(
                name=str(temp_df.iloc[i, 0]), pos=str(temp_df.iloc[i, 1]), age=float(temp_df.iloc[i, 2]),
                tm=str(temp_df.iloc[i, 3]), g=float(temp_df.iloc[i, 4]), gs=float(temp_df.iloc[i, 5]),
                mp=float(temp_df.iloc[i, 6]), fg=float(temp_df.iloc[i, 7]),fga=float(temp_df.iloc[i, 8]),
                fg_percent=float(temp_df.iloc[i, 9]), three_point=float(temp_df.iloc[i, 10]), three_point_a=float(temp_df.iloc[i, 11]),
                three_point_percent=float(temp_df.iloc[i, 12]), two_point=float(temp_df.iloc[i, 13]), two_point_a=float(temp_df.iloc[i, 14]),
                two_point_percent=float(temp_df.iloc[i, 15]),efg=float(temp_df.iloc[i, 16]), ft=float(temp_df.iloc[i, 17]), 
                fta=float(temp_df.iloc[i, 18]), ft_percent=float(temp_df.iloc[i, 19]),orb=float(temp_df.iloc[i, 20]),
                drb=float(temp_df.iloc[i, 21]), trb=float(temp_df.iloc[i, 22]), ast=float(temp_df.iloc[i, 23]),
                stl=float(temp_df.iloc[i, 24]), blk=float(temp_df.iloc[i, 25]), tov=float(temp_df.iloc[i, 26]), 
                pf=float(temp_df.iloc[i, 27]), pts=float(temp_df.iloc[i, 28]))
            db.session.add(entry)
            db.session.commit()
instance=ReadCsv()

@app.route("/")

def index():
    return render_template("index.html")

# can look up the error codes online
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/players")

def players():
    
    players_table=Players.query.order_by(Players.name)
    return render_template("players.html", players_table=[temp_df.to_html(classes=["internal-table-container"],index=False)], header=True)



# class InsertPlayer:
#     def __init__(self, id, name, pos, age, team, g, mp,
#                 fgp, tpp, rb, ass, stl, blk, tur, fwl, pts ):
#         self.id=id
#         self.name-name
#         self.pos=pos
#         self.age=age
#         self.team=team
#         self.g=g
#         self.mp=mp
#         self.fgp=fgp
#         self.tpp=tpp
#         self.rb=rb
#         self.ass=ass
#         self.stl=stl
#         self.blk=blk
#         self.tur=tur
#         self.fwl=fwl
#         self.pts=pts