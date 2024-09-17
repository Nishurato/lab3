import psycopg2

conn = psycopg2.connect(dbname="site", user="postgres", password="ma0505", host="localhost")
cursor = conn.cursor()

conn.autocommit = True

cursor.execute("INSERT INTO usersite (name, tel, date) VALUES ('max', '+7', NOW())")
cursor.close()
conn.close()
