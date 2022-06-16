import math
print()
print("Veuillez entrer les coordonnées du point a ")
print()
Xa=float(input("Xa : "))
Ya=float(input("Ya : "))
print()
print("Veuillez entrer les coordonnées du point b ")
Xb=float(input("Xb : "))
Yb=float(input("Yb : "))

def distance(Xa,Xb,Ya,Yb):
    Dx=Xb-Xa
    Dy=Yb-Ya
    distance=math.sqrt((Dx**2)+(Dy**2))
    return distance

print(distance(Xa,Xb,Ya,Yb))