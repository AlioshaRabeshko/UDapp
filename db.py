import sqlite3
import re


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS patients (id INTEGER PRIMARY KEY, name TEXT, birthDate DATE, livingPlace TEXT, sex TEXT)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM patients")
        rows = self.cur.fetchall()
        return rows

    def getById(self, name):
        self.cur.execute("SELECT * FROM patients WHERE id = \"%s\"" % (name))
        rows = self.cur.fetchall()
        return rows

    def fetchByName(self, searchingName):
        return list(filter(lambda name: len(re.findall(
            searchingName, name[1])) > 0, self.fetch()))

    def insert(self, data):
        self.cur.execute("INSERT INTO patients VALUES (NULL, ?, ?, ?, ?)",
                         (data['name'], data['birthday'], data['livingPlace'], data['sex']))
        self.conn.commit()

    def delete(self, id):
        pass

    def update(self, id, data):
        pass

    def __del__(self):
        self.conn.close()


# db = Database('patients.db')
# db.insert({'name': 'Абешко Олексій Михайлович',
#            'birthday': '29/03/2000', 'livingPlace': 'Дубровиця', 'sex': 'ч'})
# db.insert({'name': 'Бешко Олексій Михайлович',
#            'birthday': '29/03/2000', 'livingPlace': 'Дубровиця', 'sex': 'ч'})
# db.insert({'name': 'Ешко Олексій Михайлович',
#            'birthday': '29/03/2000', 'livingPlace': 'Дубровиця', 'sex': 'ч'})
# db.insert({'name': 'Арбешко Олексій Михайлович',
#            'birthday': '29/03/2000', 'livingPlace': 'Дубровиця', 'sex': 'ч'})
# db.insert({'name': 'Шко Олексій Михайлович',
#            'birthday': '29/03/2000', 'livingPlace': 'Дубровиця', 'sex': 'ч'})
