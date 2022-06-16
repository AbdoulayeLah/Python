

class rectangle():
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur

    @property
    def perimetre(self):
        return 2*(self.longueur + self.largeur)

    @property
    def surface(self):
        return (self.longueur * self.largeur)


class parallelopipede(rectangle):
    def __init__(self,longueur,largeur,hauteur):
        self.hauteur=hauteur
        rectangle.__init__(self,longueur,largeur)


    def volume(self):
        return (self.longueur * self.largeur)*self.hauteur


rectangle1=rectangle(6,2)
parallelopipede1=parallelopipede(6,2,12)



#print(f"longueur = {rectangle1.longueur} largeur = {rectangle1.largeur} parallelopipede = {parallelopipede1.hauteur}")
#print(f"le perimetre du rectangle est {rectangle1.perimetre()}")
#print(f"la surface du rectangle est {rectangle1.surface()}")
#print(f"le volume du  est parallelopipede  est {parallelopipede1.volume()}")

rectangle1.largeur=25

print(rectangle1.longueur)
print(rectangle1.largeur)
print(parallelopipede1.hauteur)
print(rectangle1.perimetre)
print(rectangle1.surface)
print(parallelopipede1.volume())



#
#car={
#    "longueur":rectangle1.longueur,
#    "largeur":rectangle1.largeur,
#    "volume":parallelopipede1.hauteur
#
#
#}
#
#x=car.get("longueur")
#print(x)
#