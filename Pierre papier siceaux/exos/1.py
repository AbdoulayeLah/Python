#{}[]*/\><
import random
a=str
membre=[]
while a!="fin":
    a=input("Entrer un membre : ")
    membre.append(a)
del membre[-1]
b=str
b=random.choice(membre)
print(membre)
print(b)


