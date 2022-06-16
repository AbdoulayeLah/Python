print()
t=0
while t==0:

    age=int(input("Veuillez saisir votre age : "))
    def Catégorie(age):
        if age==6 or age==7:
            print("Poussin")
        elif age==8 or age==9:
            print("Pupille")
        elif age==10 or age==11:
            print("Minime")
        elif 12<=age<=16:
            print("Cadet")
        else:
            print("Hors cathégorie")

    Catégorie(age)