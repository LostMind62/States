import sqlite3 as sql

def createdb():
    conn=sql.connect("states.db")
    conn.commit()
    conn.close()
    
def createTable():
    conn=sql.connect("states.db")
    cur= conn.cursor()
    cur.execute(
        """CREATE TABLE state (ID integer primary key, region varchar(20), city_name varchar(20) , lenguage varchar(20), time REAL); """
    )

if __name__ =="__main__":
    createdb()