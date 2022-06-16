
L=int(input("Entrer la Longueur du rectangle : "))
print()
l=int(input("Entrer la largeur du rectangle : "))

def péri(L,l):
    périmétre=(L+l)*2
    surface=L*l
    print(f"Le périmètre du rectangle est {périmétre}, et sa surface est {surface} ")
    
péri(L,l)

