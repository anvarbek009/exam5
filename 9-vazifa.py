import requests
import psycopg2
from multiprocessing import Process, Pool
from psycopg2 import sql
conn = psycopg2.connect(dbname='users', host='localhost', port='5432', user='postgres', password='03252009')
curr = conn.cursor()
url = "https://dummyjson.com/products"
response = requests.get(url)
data = response.json()
create_table_query = """
    CREATE TABLE IF NOT EXISTS currency_exchange_rates (
        id SERIAL PRIMARY KEY,
        title VARCHAR(32) NOT NULL,
        description VARCHAR(255) NOT NULL,
        price VARCHAR(255) NOT NULL,
        discountPercentage VARCHAR(255) NOT NULL,
        rating VARCHAR(255) NOT NULL,
        stock VARCHAR(255) NOT NULL,
        brand VARCHAR(32),
        category VARCHAR (32),
        thumbnail VARCHAR(32),
        images VARCHAR(256)
    )
"""
curr.execute(create_table_query)
conn.commit()
for item in data:
    insert_query = sql.SQL("""
        INSERT INTO currency_exchange_rates (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail, images)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """)
    curr.execute(insert_query, (item['title'], item['description'], item['price'], item['discountPercentage'], item['rating'], item['stock'], item['brand'], item['category'], item['thumbnail'], item['images']))
    conn.commit()
conn.commit()
conn.close()