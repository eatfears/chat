import sqlite3
from os import path

ROOT = path.dirname(path.realpath(__file__))


class Database:
    db = None

    def __init__(self):
        self.db = sqlite3.connect(path.join(ROOT, "chat.db"))
        pass

    def create_scheme(self):
        curs = self.db.cursor()
        try:
            curs.execute("DROP TABLE users")
            curs.execute("DROP TABLE messages")
        except:
            pass
        curs.execute("CREATE TABLE users(id_vk INTEGER PRIMARY KEY, cur_step INTEGER)")
        curs.execute("CREATE TABLE messages(id INTEGER PRIMARY KEY, message STRING)")

    def add_user(self, username):
        curs = self.db.cursor()
        curs.execute("INSERT INTO users(id_vk, cur_step) VALUES (?, ?)", (username, 0))
        self.db.commit()

    def add_message(self, string):
        curs = self.db.cursor()
        curs.execute("INSERT INTO messages(message) VALUES (?)", [string])
        self.db.commit()


# db = Database()
# db.create_scheme()
# db.add_user(666)
# db.add_user(555)
