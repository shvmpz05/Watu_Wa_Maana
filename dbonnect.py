import sqlite3

class DBConnection:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

db = DBConnection("WWM_inventory.db")
