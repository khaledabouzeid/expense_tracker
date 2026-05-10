import sqlite3
import sys






class expense:
    def __init__(self, category, amount, currency):
        self.category=category
        self.amount= amount
        self.currency=currency

    def save(self, amount_in_base):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (category, amount, currency, amount_in_base) VALUES (?,?,?,?)",(self.category,self.amount,self.currency, amount_in_base)  )
        conn.commit()
        conn.close()
       