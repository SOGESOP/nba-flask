import os
import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="nba",    
    user=os.environ["DB_USERNAME"],
    password=os.environ["DB_PASSWORD"]
)

cur=conn.cursor()

cur.execute("CREATE TABLE players (id serial PRIMARY KEY,"
                                        "name varchar(50),"
                                        "pos varchar(2),"
                                        "age float,"
                                        "tm varchar(3),"
                                        "g integer,"
                                        "gs integer,"
                                        "mp float,"
                                        "fg float,"
                                        "fga float,"
                                        "fg_percent float,"
                                        "three_point_m float,"
                                        "three_point_a float,"
                                        "three_point_percent float,"
                                        "two_point_m float,"
                                        "two_point_a float,"
                                        "two_point_percent float,"
                                        "efg float,"
                                        "ftm float,"
                                        "fta float,"
                                        "ft_percent float," 
                                        "orb float,"
                                        "drb float,"
                                        "trb float,"
                                        "ast float,"
                                        "stl float,"
                                        "blk float,"
                                        "tov float,"
                                        "pf float,"
                                        "pts float);"
                                )

conn.commit()
cur.close()
conn.close()