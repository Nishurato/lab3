import psycopg2

conn = psycopg2.connect(dbname="site", user="postgres", password="ma0505", host="localhost")
cursor = conn.cursor()

conn.autocommit = True

cursor.execute('CREATE TABLE usersite (id SERIAL PRIMARY KEY, name varchar(256), tel varchar(256), date DATE)')
cursor.close()
conn.close()
