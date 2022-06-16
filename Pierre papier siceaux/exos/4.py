n=int(input("saisir un entier :  "))
x=True
if n>0:
    ch=str(n)
    for i in ch:
        if ch.count(i)>1:
            x=False
            break
    
    
    if x==True:
        print(f"{n} est distinct")
    else:
        print(f"{n} est non distinct")
else:
    print("saisir un entier positif")
