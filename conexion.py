import sqlite3 as sql
# metodos base de datos

def createdb():
    conn=sql.connect("states.db")
    conn.commit()
    conn.close()
    
def createTable():
    conn=sql.connect("states.db")
    cur= conn.cursor()
    cur.execute(
        """CREATE TABLE state (ID integer primary key, region varchar(255), city_name varchar(20) , lenguage varchar(20), time REAL); """
    )
    conn.commit()
    conn.close()

def inserts(i):
    conn=sql.connect("states.db")
    cur= conn.cursor()
    print(type(i))
    if i != []:
        for x in i:
            for y in x:
                    qery="INSERT INTO state (id,region,city_name,lenguage,time) VALUES (NULL,'" + y['region'] + "','"+ y['city name'] + "','"+ y['Lenguaje']+ "'," + str(y['Time']) +")"
                    cur.execute(qery)
                    conn.commit()
    conn.close()

    