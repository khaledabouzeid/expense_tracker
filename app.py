from helpers import transform_to_base
from flask import Flask, request, render_template, redirect, url_for
from models import expense
import sqlite3

app = Flask(__name__)

CATEGORIES = [
    "Food",
    "Housing",
    "Transportation",
    "Health", 
    "Education"
]

CURRENCIES= [
    "EGP"
]

@app.route("/")
def start():
    return render_template("start.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method =="POST":
        category = request.form.get("category")
        amount = request.form.get("amount")
        amount= float(amount)
        currency = request.form.get("currency")

        # validation
        
       
        if category not in CATEGORIES:
            return render_template("error.html", message="Invalid category")

       
        
        if amount < 0:
            return render_template("error.html", message="Invalid amount")

        else:
            amount_m = round(amount, 2)


        if currency not in CURRENCIES:
            return render_template("error.html", message="Invalid currency")


       

        amount_in_base=transform_to_base(currency,  amount_m)
        new_expense = expense(category, amount_m, currency)
        new_expense.save(amount_in_base)

        return redirect(url_for("total"))
       

    return render_template("add.html", category=CATEGORIES, currency=CURRENCIES)

@app.route("/total_usd")
def total_usd():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    total= cursor.execute("SELECT sum(amount_in_base) FROM expenses").fetchone()
    conn.close()
    return render_template("total_usd.html", total_usd=total)

@app.route("/total")
def total():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    total= cursor.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    return render_template("total.html", total=total)
