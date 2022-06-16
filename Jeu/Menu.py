from base_de_donnée.données import Se_connecter

données=Se_connecter("mabase.db")

def registre():
    username=input("Identifiant : ")
    password=input("Mot de passe : ")

    données.creation_personne(username, password)








def menu():
    while True:
        print("---MENU---")
        print("1-S'enregistrer")
        print("2-Paramètre")
        choix=int(input())

        if choix==1:
            registre()

menu()