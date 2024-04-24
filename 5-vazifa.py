import psycopg2
from psycopg2 import sql
def connect(dbname,host,user,password,tablename):
    conn = psycopg2.connect(dbname=dbname, host=host, port='5432', user=user, password=password)
    curr = conn.cursor()
    def select(tablename):
        alll=curr.execute(f"SELECT * FROM {tablename}")
    print(select(tablename))
    conn.commit()
    conn.close()

connect('users','localhost','postgres','03252009','users')
