rayon=float(input("Veuillez entrer le rayon du sphère : "))



def volume(rayon):
    volume=(4*3.14*(rayon**3))/3
    return volume

print("Le volume du sphère est : ",volume(rayon))