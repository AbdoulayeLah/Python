import os
import sqlite3

class classconnexion():
    def __init__(self, database_name : str):
        self.con=sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.con.row_factory= sqlite3.Row

    def create_compte(self,nom, numeroCompte, solde):
        cursor=self.con.cursor()
        query=f"INSERT INTO Utilisateurs (nom, numeroCompte, solde) VALUES ('{nom}','{numeroCompte}','{solde}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

