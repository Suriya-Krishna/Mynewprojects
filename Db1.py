import sqlite3
def db_connect():
    conn = sqlite3.connect('Car_new.db')
    return conn

def create_table():
      con = db_connect()
      cur = con.cursor()
      query = """CREATE TABLE CARS(NAME_OF_CAR CHAR(60) NOT NULL, NAME_OF_OWNER CHAR(100) NOT NULL)"""
      cur.execute(query)
      con.commit()
      con.close()

def add_data():
    con = db_connect()
    cur = con.cursor()
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('HYUNDAI','RAM')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('TOYOTA','SAM')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('DUSTER','PREM')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('SUZUKI','HARI')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('HONDA','NILA')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('HYUNDAI','DEV')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('BMW','KUMAR')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('WAGON','LILLY')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('HONDA','SAMMY')")
    cur.execute("INSERT INTO CARS(NAME_OF_CAR,NAME_OF_OWNER)""VALUES('SUZUKI','KIRAN')")
    con.commit()
    con.close()


con = db_connect()
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS CARS")
create_table()
add_data()
cur.execute("SELECT * from CARS")
print(cur.fetchall())
conn.close()
