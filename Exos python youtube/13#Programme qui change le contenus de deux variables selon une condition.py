A=float(input("A = "))
B=float(input("B = "))

def Condition(A,B):
    if A*B>=0:
        A,B=B,A
        print("A = ",format(A,".1f"))
        print("B = ",format(B,".1f"))
    elif A*B<0: 
        A,B=(A+B),(A*B)
        print("A = ",format(A,".1f"))
        print("B = ",format(B,".1f"))
    else:
        print("Données non numérique")

Condition(A,B)
