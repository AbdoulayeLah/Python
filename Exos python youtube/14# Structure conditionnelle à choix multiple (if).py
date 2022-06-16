num=int(input("Veuillez entrer le nombre de photocopies effectuées : "))
def facture(num):
    if 0<num<=10:
        facture=0.30*num
        print(f"La facture pour {num} photocopies est de {facture} dh")
    elif 10<num<=30:
        facture=(0.25*(num-10)+(0.30*10))
        print(f"La facture pour {num} photocopies est de {facture} dh")
    elif num>30:
        facture=(0.20*(num-30)+(0.25*20)+(0.30*10))
        print(f"La facture pour {num} photocopies est de {facture} dh")
    else:
        print("Erreur de saisie")
    

facture(num)