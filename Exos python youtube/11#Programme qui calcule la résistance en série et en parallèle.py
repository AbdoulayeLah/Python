def a():
    print()
a()
R1=float(input("Veuillez saisir la valeur de R1 :  "))
a()
R2=float(input("Veuillez saisir la valeur de R2 :  "))
a()
R3=float(input("Veuillez saisir la valeur de R3 :  "))


def résistance(R1:float,R2:float,R3:float,):
    a()
    Rser=R1+R2+R3
    print(f"La résistance en série est : ",format(Rser,".2f"))
    
    Rpar=(R1*R2*R3)/((R2*R3)+(R1*R3)+(R1*R2))
    a()
    print("La résistance en parallèle est : ",format(Rpar,".2f"))
    a()

a()
résistance(R1,R2,R3)
