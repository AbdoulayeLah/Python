import random
a=[1,2,3,4,5]
print(random.choice(a))

#oubien

from random import choice
liste=[]
b=2
print("Le 0 stop la liste")
while b!=0:
    b=int(input("Entrer des nombres au hasard : "))
    liste.append(b)
liste.sort()
print(liste)
print(choice(a))