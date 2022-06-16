

A=input("Age : ")
vrf=A.isdigit()
while vrf== False:
    print("Erreur de saisit")
    A=input("Age : ")
    vrf=A.isdigit()

age=int(A)


sexe=input("Sexe (H/F) : ")
while sexe != "H" and sexe != "F":
    print("Erreur de saisie")
    sexe=str(input("Sexe (H/F) : "))
   
    



def impot(age,sexe):
    if (sexe=="H" and age > 20) or (sexe=="F" and 18<= age <=35):
        print("L'habitant est imposable")
    else:
        print("L'habitant n'est pas imposable")
        

impot(age,sexe)

