"""
    pip install psycopg2
    create new index.py file
    add the following code
"""

# psycopg2 is a Postgres database adapter for Python
import psycopg2
conn = psycopg2.connect(user="postgres", password="postgres", dbname="shopping")

# cursor object allows Python to execute 
# commands in a database session
cur = conn.cursor()
cur.execute("INSERT INTO Products (name) values ('a')") 
cur.execute("INSERT INTO Products (name) values ('b')") 
conn.commit()

cur.execute("SELECT * FROM products")
products = cur.fetchall()
for product in products :
    print (product[1])

conn.close()
