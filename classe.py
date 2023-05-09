import sqlite3

conn = sqlite3.connect("./moko.db")

cur = conn.cursor()

class Student:

    def __init__(self):
        self.conn = sqlite3.connect("./moko.db")
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS student(
        id INTEGER  PRIMARY KEY,
        nom TEXT,
        age INTEGER,
        classe TEXT
        )''')

    def add_student(self, nom, age,classe):
        self.cur.execute("""INSERT INTO student(nom, age, classe) VALUES(?, ?, ?)""", (nom, age, classe))
        self.conn.commit()

    def get_all_student(self):
        self.cur.execute('''SELECT * FROM student''')
        students = self.cur.fetchall()
        return students 
     
    def get_student(self, id):
        self.cur.execute(f"SELECT nom, age, classe FROM student WHERE id={id}")
        student = self.cur.fetchone()
    
        return student if student else False

    def update(self, id, nom, age, classe):
        self.cur.execute(f"UPDATE student SET nom = '{nom}', age = {age}, classe = '{classe}' WHERE id = {id}")
        # self.cur.execute("UPDATE student SET nom=?, age=?, classe=? WHERE id=?", (nom,age,classe,id))
        self.conn.commit()


    def delete(self,id):
        self.cur.execute(f"DELETE FROM student WHERE id = {id}")
        self.conn.commit()

