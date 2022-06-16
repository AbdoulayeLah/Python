PHT=float(input("PRIX HT : "))
CAT=input("Catégorie (A/B/C) : ")
while CAT!="A" and CAT!="B" and CAT!="C" :
    print("Erreur de saisie") 
    CAT=input("Catégorie (A/B/C) : ")

def Prix_TTC(PHT,CAT):
    if CAT=="A":
        Prix_TTC=PHT+PHT*0.07
        print(f"PRIX TTC : {Prix_TTC}")
    elif CAT=="B":
        Prix_TTC=PHT+PHT*0.2
        print(f"PRIX TTC : {Prix_TTC}")
    else:
        Prix_TTC=PHT+PHT*0.25
        print(f"PRIX TTC : {Prix_TTC}")

Prix_TTC(PHT,CAT)