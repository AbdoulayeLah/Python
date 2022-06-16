import random
# la fonction join() et random.sample->échantillon
print("-----GENERATEUR DE MOT DE PASSE-----")
t=0
while t==0:

    lettre_min="abcdefghijklmnopqrstuvwxyz"
    lettre_maj="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num="0123456789"
    symbole="!@#$%^&*()\/,;:!§.?'-_=^*ùéçàµ£¨+°<>"

    concaténation = lettre_min + lettre_maj + num + symbole

    taille=int(input("Taille : "))

    password="".join(random.sample(concaténation,taille))

    print(password)
    

    
    