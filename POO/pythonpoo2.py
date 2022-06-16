import time
from docdata.bdpythonpoo2 import *

seconnecter=classconnexion("mondatabase.db")

class compteBancaire():
    def __init__(self,numeroCompte : int,nom : str,solde : float):
        self.numeroCompte=numeroCompte
        self.nom=nom
        self.solde=solde


    def versement(self,argent):
        self.solde=self.solde+argent
        return self.solde
        


    def retrait(self,argent):
        if (self.solde < argent):
            print("impossible d'effectuer l'opération, votre solde est insuffisant")
            print()
        else:
            self.solde=self.solde-argent

        return self.solde
        
        
    

    def agios(self):
        self.solde=(self.solde*95)/100
        return self.solde
        
        

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"NumeroCompte : {self.numeroCompte}")
        print(f"Solde : {self.solde}")



def menu():
    while True:
        nom=input("Nom : ")
        numeroCompte=int(input("NumeroCompte : "))
        solde=float(input("Solde : "))

        seconnecter.create_compte(nom, numeroCompte, solde )

        compte=compteBancaire(numeroCompte,nom,solde)

        time.sleep(1)
        print("---MENU---")
        print("1) Versement sur votre compte")
        print("2) Retrait sur votre compte")
        print("3) Appliquer Agios")
        choix=int(input("choix : "))
        time.sleep(1)
        montant=int(input("montant : "))
        time.sleep(1)

        if choix==1:
            compte.versement(montant)
            compte.afficher()

        elif choix==2:
            compte.retrait(montant)
        
            compte.afficher()
    
        elif choix==3:
            compte.agios()
        
            compte.afficher()
    
        else:
            print("Erreur de saisie")





menu()




