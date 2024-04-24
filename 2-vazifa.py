import psycopg2
from decimal import Decimal

conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

cur = conn.cursor()

data = (1, "Samsung A72", Decimal('452.12'), "black")
cur.execute("INSERT INTO Product (id, name, price, color) VALUES (%s, %s, %s, %s)", data)

conn.commit()

cur.close()
conn.close()