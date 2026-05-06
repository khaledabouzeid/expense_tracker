import sqlite3

class expense:
    def __init__(self, category, amount, currency):
        self.category=category
        self.amount= amount
        self.currency=currency