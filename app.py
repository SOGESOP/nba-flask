from flask import Flask, render_template, flash
from datetime import datetime
import pandas
import os
import psycopg2
app=Flask(__name__)
def get_db_connection():
    conn=psycopg2.connect(host="localhost",
                          database="nba",
                          user=os.environ["DB_USERNAME"],
                          password=os.environ["DB_PASSWORD"]
    )
    return conn
    
app.app_context().push()
    

@app.route("/")
def index():
    return render_template("index.html")

# can look up the error codes online
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404



@app.route("/players")
def players():
    sql_to_pandas()
    players_table=[df.to_html(classes="data")]

    return render_template("players.html", players_table=players_table)

check the postgres database includes the column labels