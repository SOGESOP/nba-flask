import os
import psycopg2
import pandas


def get_db_connection():
    conn=psycopg2.connect(host="localhost",
                          database="nba",
                          user="theodore",
                          password="pierre"
    )
    return conn
    
    
    
def sql_to_pandas():
    global df
    df=pandas.DataFrame()
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM players")
    players_table:list[tuple]=cur.fetchall()
    cur.close()
    conn.close()
    for player_info in players_table:
        df=pandas.concat([df, pandas.DataFrame([player_info])], ignore_index=True, )
        
i need to add the column labels and then also remove the extra index column
sql_to_pandas()
