from flask import Flask, render_template, request

import requests
import psycopg2
import datetime

app = Flask(__name__)

conn = psycopg2.connect(dbname="site", user="postgres", password="ma0505", host="127.0.0.1")
cursor = conn.cursor()

conn.autocommit = True

@app.route("/", methods=['GET', 'POST'])
def form():
    return render_template('main.html')

if __name__== 'main':
    app.run()

@app.route("/submitted", methods=['GET', 'POST'])
def second_page():
    phone_data = request.form["phone"]
    name_data = request.form["name"]
    cursor.execute("INSERT INTO usersite (name, tel, date) VALUES (%s, %s, %s)", (name_data, phone_data, datetime.datetime.now()))
    cursor.close()
    conn.close()
    return render_template("page2.html")

