## market.py ##

from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import connect

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgressql://postgres:password@localhost/MiniMart'

db = SQLAlchemy(app)

app.run()

# http://127.0.0.1:5000/

@app.route('/')
@app.route('/home')
def home_page():
    conn = connect(host="localhost", database="MiniMart", user='postgres', password='password')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Store;')
    stores = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', stores=stores)


@app.route('/customers')
def customer_page():
    conn = connect(host="localhost", database="MiniMart", user='postgres', password='password')
    cur = conn.cursor()
    cur.execute('SELECT * FROM customer;')
    customers = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('customers.html', customers=customers)


@app.route("/customers/update/<customer_id>")
def update_customer(customer_id):
    return render_template('update.html', customer_id=customer_id)


@app.route("/customers/update/phh/<customer_id>", methods = ["POST"])
def update_phh(customer_id):
    customer_phone_number = request.form["phh"]
    conn = connect(host="localhost", database="MiniMart", user='postgres', password='password')
    cur = conn.cursor()
    cur.execute(f'UPDATE customer SET customer_phone_number = {customer_phone_number} WHERE customer_id = {customer_id};')
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/customers")



