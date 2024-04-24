import psycopg2
from multiprocessing import Process, Pool
conn = psycopg2.connect(dbname='users', host='localhost', port='5432', user='postgres', password='03252009')
curr = conn.cursor()
def select(tablename):
    b=curr.execute(f'SELECT * FROM {tablename}')
    print(b)

if __name__ == '__main__':
    with Pool(4) as p:
        s=['users']
        p.map(select,s)   

conn.commit()
conn.close()    