import os
import sqlite3


class Se_connecter():
    def __init__(self, nom_base : str):
        self.con=sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{nom_base}")
        self.con.row_factory=sqlite3.Row

    def creation_personne(self,username : str, password : str):
        cursor=self.con.cursor()

        query=f"INSERT INTO matable (username, password) VALUES ('{username}','{password}'); "

        cursor.execute(query)
        cursor.close()
        self.con.commit
        