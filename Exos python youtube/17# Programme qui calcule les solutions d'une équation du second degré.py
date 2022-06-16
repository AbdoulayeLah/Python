from configparser import RawConfigParser
import math
t=0
while t==0:
    print("----------EQUATION DU SECOND DEGRES----------")
    print("               aX2 + bX + c = 0              ")
    a=int(input("a = "))
    b=int(input("b = "))
    c=int(input("c = "))
    print(f"            {a}X2 + {b}X + {c} = 0           ")

    def racine(delta):
        racine=math.sqrt(delta)
        return racine

    delta=(b**2)-(4*a*c)

    def second_degrès(a,b,c):
        if delta<0:
            print("Pas de solution")
        elif delta ==0:
            X=(-b)/(2*a)
            print("S = ",format(X,".2f"))
        else:
            X1=((-b)-(racine(delta)))/(2*a)
            X2=((-b)+(racine(delta)))/(2*a)
            print("S = ",format(X1,".2f")," ; ",format(X2,".2f")," ")



    second_degrès(a,b,c)
