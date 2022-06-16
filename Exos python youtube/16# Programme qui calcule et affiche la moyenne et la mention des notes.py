boucle=0
while  boucle==0: 
    def alaligne():
        print()
    alaligne()
    nom=str(input("NOM : "))
    alaligne()
    prenom=str(input("PRENOM : "))
    alaligne()
    print(f"----------BULLETIN DE {prenom} {nom}----------")
    alaligne()
    def vérification(note):
        note=float(input("Note : "))
        if note<0 or note>20:
            print("Erreur de saisie ")
            note=float(input("Note : "))
        return note
    note_1=vérification(1)
    alaligne()
    note_2=vérification(1)
    alaligne()
    note_3=vérification(1)
    alaligne()
    def Moyenne(note_1,note_2,note_3):
        Moyenne=float((note_1+note_2+note_3)/3)
        if Moyenne<10:
            print("Mention Insuffisant : Moyenne",format(Moyenne,".2f"))
            alaligne()
        elif 10<=Moyenne<12:
            print("Mention Passable : Moyenne",format(Moyenne,".2f"))
            alaligne()
        elif 12<=Moyenne<14:
            print(f"Mention Assez Bien : Moyenne",format(Moyenne,".2f"))
            alaligne()
        elif 14<=Moyenne<16:
            print("Mention Bien : Moyenne",format(Moyenne,".2f"))
            alaligne()
        else:
            print("Mention Très Bien : Moyenne",format(Moyenne,".2f"))
            alaligne()
    Moyenne(note_1,note_2,note_3)
