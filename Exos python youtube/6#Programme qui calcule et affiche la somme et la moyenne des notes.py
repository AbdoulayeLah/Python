somme=0
for i in range(0,5):
    try:
        i=float(input(f"Note {i} : "))
        somme=somme+i
    except:
        print("Erreur de saisie")    
moyenne=somme/5   
print(f"Somme : {somme}")
print(f"moyenne : {moyenne}")
    
    
