import random
choix=input("Entrer votre choix : ")
point=0
while choix!="stop":
    
    liste=["pierre","papier","ciseaux"]
    aléatoire=random.choice(liste)
    print(f"choix de l'ordinateur : {aléatoire}")

    if choix=="pierre" and aléatoire=="papier":
        print("perdu")
        point-=2
        choix=input("Entrer votre choix : ")
    elif choix=="papier" and aléatoire=="pierre":
        print("win")
        point+=2
        choix=input("Entrer votre choix : ")
    elif choix=="ciseaux" and aléatoire=="pierre":
        print("perdu")
        point-=2
        choix=input("Entrer votre choix : ")
    elif choix=="pierre" and aléatoire=="ciseaux":
        print("win")
        point+=2
        choix=input("Entrer votre choix : ")
    elif choix=="ciseaux" and aléatoire=="papier":
        print("win")
        point+=2
        choix=input("Entrer votre choix : ")
    elif choix=="papier" and aléatoire=="ciseaux":
        print("perdu")
        point-=2
        choix=input("Entrer votre choix : ")
    elif choix==aléatoire:
        print("rejouer")
        choix=input("Entrer votre choix : ")
    else:
        print("Erreur de saisie")
        choix=input("Entrer votre choix : ")

if point<=0:
    print(f"vous avez 0 points")
else:
    print(f"vous avez {point} points")