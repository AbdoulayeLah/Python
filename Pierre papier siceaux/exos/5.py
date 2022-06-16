a=1
liste=[]
print(" taper le nombre 0 permet d'arrter la saisie,merci " )
while a!=0:
    a=int(input("Entrer une donnée : "))
    liste.append(a)
    

del liste[-1]
print(liste)


debin=0
fin=4

debin=int(input("Entrer le début de la ranger : "))
fin=int(input("Entrer la fin de la ranger : "))

debut=debin-1

def sompart(liste):
    so = 0
    for i in range(debut,fin):
        so = so + liste[i]
    return so

print("la somme de ces colonnes est de : "+repr(sompart(liste))+"")

def moypart(liste):
    si=sompart(liste)
    effectif = fin-debut
    return si/effectif

print("la moyenne de ces colonnes est de : "+repr(moypart(liste))+"")