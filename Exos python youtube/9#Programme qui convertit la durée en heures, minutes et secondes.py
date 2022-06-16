T=int(input("Entrer une durée en seconde : "))
def durée(T):
    H=T//3600
    M=(T%3600)//60
    S=(T%3600)%60
    print(f"{H}:{M}:{S}")

durée(T)
