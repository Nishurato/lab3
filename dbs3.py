import psycopg2

conn = psycopg2.connect(dbname="site", user="postgres", password="ma0505", host="localhost")
cursor = conn.cursor()

conn.autocommit = True

print(cursor.execute('SELECT * FROM usersite'))
cursor.close()
conn.close()
