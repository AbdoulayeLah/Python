liste=[]
a=1
print("Le 0 permet d'arreter la saisie")

while a!=0:
    a=int(input("Entrer une donnée : "))
    liste.append(a)

del liste[-1]

print(liste)

déb=1
fin=1
finin=1
débin=1
débin=int(input("Entrer la colonne de début : "))
finin=int(input("Entrer la colonne de fin : "))

fin=finin+1
déb=débin-1

def sompart(liste):
    s=0
    for i in range(déb,finin):
        s=s+liste[i]
    return s

print(sompart(liste))






def moyenne(liste):
   nomb=finin-déb
   return sompart(liste)/nomb

print(moyenne(liste))