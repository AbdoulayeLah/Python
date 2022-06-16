def a():
    print()
a()
num1 =float(input(" Veuillez entrer la première valeur : "))
a()
num2 =float(input(" Veuillez entrer la deuxième valeur : "))
a()
def Valeur(num1,num2):
    
    if (num1*num2) >= 0:
        print(" Les deux nombres sont de même signe ")
        a()
    elif (num1*num2) < 0:
        print(" Les deux nombres sont de signes contraires ")
        a()
    else:
        print("Erreur de saisie")
        a()

Valeur(num1,num2)